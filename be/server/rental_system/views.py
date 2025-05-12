import datetime
import json

from django.db import transaction
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response
from drf_spectacular.utils import extend_schema

from .models import Rental
from book_copy.models import BookCopy
from .serializers import RentalRequestSerializer, RentalResponseSerializer
from utils.redis import redis_client
# Create your views here.


def rent_book(user_id, book_ids):
    with transaction.atomic():
        user = get_user_model().objects.get(pk=user_id)
        if not user:
            raise ValueError("User Not Found!")
        rentals = []
        # Get the available Copy ID from book
        # set the available copy status as on loan
        # Create the rental row
        for book_id in book_ids:
            book_copy = (
                BookCopy.objects.select_for_update(skip_locked=True)
                .filter(book=book_id, status="available")
                .first()
            )
            if not book_copy:
                return ValueError(f"No available copies for book id {book_id}")
            book_copy.status = "on_loan"
            book_copy.save()

            # create rental
            today = datetime.date.today()
            rental = Rental.objects.create(
                borrow_date=today,
                expected_date=today + datetime.timedelta(days=30),
                copy=book_copy,
                cust=user,
            )
            rentals.append(rental)
            return rentals


class RentalView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Rental.objects.all()

    @extend_schema(
        tags=["rental"],
        request=RentalRequestSerializer,
        responses={status.HTTP_201_CREATED: RentalResponseSerializer},
    )
    def post(self, request):
        user_id = self.request.user.id
        book_ids = request.data.get("book_ids")
        if len(book_ids) < 1:
            return Response(
                data="No Books to Rent!", status=status.HTTP_400_BAD_REQUEST
            )

        try:
            rentals = rent_book(user_id, book_ids)
            serializer = RentalResponseSerializer({"rentals": rentals})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(str(e))
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)


class RentalCache(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(tags=["rental"], responses={status.HTTP_201_CREATED: None})
    def post(self, request):
        user_id = request.user.id
        key = f"user:{user_id}:cart"
        cart = request.data.get("books")

        if not isinstance(cart, list):
            return Response(
                {"error": "Invalid cart format"}, status=status.HTTP_400_BAD_REQUEST
            )

        try:
            redis_client.setex(key, 60 * 60 * 24, json.dumps(cart))  # 24 hours
            return Response(
                status=status.HTTP_201_CREATED if cart else status.HTTP_204_NO_CONTENT
            )
        except Exception as e:
            # Optional logging
            print.error(f"Redis set error for user {user_id}: {e}")
            return Response(
                data="Internal server error",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @extend_schema(tags=["rental"])
    def get(self, request):
        user_id = request.user.id
        key = f"user:{user_id}:cart"

        try:
            data = redis_client.get(key)
            if not data:
                return Response([], status=status.HTTP_200_OK)
            return Response(json.loads(data), status=status.HTTP_200_OK)
        except Exception as e:
            print.error(f"Redis get error for user {user_id}: {e}")
            return Response(
                data="Internal server error",
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
