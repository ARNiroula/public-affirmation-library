from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

# from user import permissions
from .models import Book
from .serializers import BookSerializer
# from utils.pagination import BookResultsPagination

# Create your views here.


@extend_schema(tags=["book"])
class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()  # pyright: ignore
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    # pagination_class = BookResultsPagination
