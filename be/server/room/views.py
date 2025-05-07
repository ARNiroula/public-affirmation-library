# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Response

from user import permissions
from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer
# Create your views here.


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()  # pyright: ignore
    serializer_class = RoomSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [permissions.IsStaff]

        return [permission() for permission in permission_classes]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()  # pyright: ignore
    serializer_class = BookingSerializer

    def get_serializer_context(self):
        ctx = super().get_serializer_context() | {"request": self.request}
        return ctx

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)  # pyright: ignore

    def get_permissions(self):
        if self.action == ("create", "list"):
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [permissions.IsOwnerOrStaff]

        return [permission() for permission in permission_classes]

    @action(detail=False, methods=["get"], permission_classes=[permissions.IsStaff])
    def all_bookings(self, request):
        queryset = Booking.objects.all()  # pyright: ignore
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
