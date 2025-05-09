import datetime

from django.db import transaction
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.views import APIView, Response
from drf_spectacular.utils import extend_schema

from user import permissions
from .models import Rental

# from book.models import Book
from book_copy.models import BookCopy
from .serializers import RentalRequestSerializer, RentalResponseSerializer
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


class RentalView(APIView, permissions.CustomerPermissionMixin):
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
            return Response(data=str(e), status=status.HTTP_400_BAD_REQUEST)
