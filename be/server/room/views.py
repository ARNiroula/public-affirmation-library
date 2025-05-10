# from django.shortcuts import render
# from django.conf import settings
# from rest_framework import status
# from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response
from drf_spectacular.utils import extend_schema

from user import permissions
from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer
# from utils.storage import minio_client
# Create your views here.


@extend_schema(tags=["room"])
class RoomViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Room.objects.all()  # pyright: ignore
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]
    # parser_classes = [MultiPartParser, FormParser]


@extend_schema(tags=["booking"])
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # pyright: ignore
    serializer_class = BookingSerializer

    def get_serializer_context(self):
        ctx = super().get_serializer_context() | {"request": self.request}
        return ctx

    def get_queryset(self):
        if self.action == "list":
            room_id = self.request.query_params.get("room_id")
            start_date = self.request.query_params.get("start_date")
            end_date = self.request.query_params.get("end_date")
            # Filter by room and the selected date range
            if room_id:
                queryset = Booking.objects.filter(room_id=room_id)  # pyright: ignore
                if start_date and end_date:
                    queryset = queryset.filter(
                        start_datetime__gte=start_date, end_datetime__lte=end_date
                    )
                return queryset

        return Booking.objects.filter(user=self.request.user)  # pyright: ignore

    def get_permissions(self):
        if self.action in ("create", "list"):
            permission_classes = [IsAuthenticated]
        elif self.action in ("all_bookings"):
            permission_classes = [permissions.IsStaff]
        else:
            permission_classes = [permissions.IsOwnerOrStaff]

        return [permission() for permission in permission_classes]

    @action(detail=False, methods=["get"], permission_classes=[permissions.IsStaff])
    def all_bookings(self, request):
        queryset = Booking.objects.all()  # pyright: ignore
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
