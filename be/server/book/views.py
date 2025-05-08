from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import Response
from drf_spectacular.utils import extend_schema

from user import permissions
from utils.storage import minio_client
from .models import Book
from .serializers import BookSerializer

# Create your views here.


@extend_schema(tags=["book"])
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [permissions.IsStaff]

        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        try:
            uploaded_file = request.data.get("file")

            if not uploaded_file:
                # Create the Book
                return Response(
                    {"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST
                )

            file_ext = uploaded_file.name.split(".")[-1].lower()
            allowed_ext = ["jpg", "jpeg", "png", "gif", "webp"]
            if file_ext not in allowed_ext:
                return Response({"error": "Unsupported file type"}, status=400)

            file_url = f"public/book/{uploaded_file}"
            try:
                minio_client.upload_fileobj(
                    Fileobj=uploaded_file,
                    Bucket=settings.AWS_STORAGE_BUCKET_NAME,
                    Key=file_url,
                    ExtraArgs={"ContentType": uploaded_file.content_type},
                )
            except Exception as e:
                return Response({"error": str(e)}, status=500)

            # Create the Book
            book = Book.objects.create(
                isbn=request.data.get("isbn"),
                name=request.data.get("name"),
                topic=request.data.get("topic"),
                pub_date=request.data.get("pub_date"),
                summary=request.data.get("summary"),
                cover_url=file_url,
            )

            serializer = self.get_serializer(book)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
