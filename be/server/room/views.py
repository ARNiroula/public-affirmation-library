# from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import Response
from drf_spectacular.utils import extend_schema

from user import permissions
from .models import Room, Booking
from .serializers import RoomSerializer, BookingSerializer
from utils.storage import minio_client
# Create your views here.


@extend_schema(tags=["room"])
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()  # pyright: ignore
    serializer_class = RoomSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [permissions.IsStaff]

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        try:
            # uploaded_file = request.FILES.get("file")
            uploaded_file = request.data.get("file")

            if not uploaded_file:
                return Response(
                    {"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST
                )
            file_ext = uploaded_file.name.split(".")[-1].lower()
            allowed_ext = ["jpg", "jpeg", "png", "gif", "webp"]
            if file_ext not in allowed_ext:
                return Response({"error": "Unsupported file type"}, status=400)

            # path = default_storage.save(f"room/{uploaded_file.name}", uploaded_file)
            # file_url = default_storage.url(path)
            file_url = f"public/room/{uploaded_file}"
            try:
                minio_client.upload_fileobj(
                    Fileobj=uploaded_file,
                    Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                    Key=file_url,
                    ExtraArgs={"ContentType": uploaded_file.content_type},
                )
            except Exception as e:
                return Response({"error": str(e)}, status=500)

            # Create the Room
            room = Room.objects.create(  # pyright: ignore
                room_id=request.data.get("room_id"),
                capacity=request.data.get("capacity"),
                descr=request.data.get("descr"),
                image_url=f"{settings.MINIO_ACCESS_URL}/{settings.AWS_STORAGE_BUCKET_NAME}/{file_url}",
            )

            serializer = self.get_serializer(room)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(str(e))
            return Response(
                "Could not create the room!", status=status.HTTP_400_BAD_REQUEST
            )
        # return super().create(request, *args, **kwargs)


@extend_schema(tags=["booking"])
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
