from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from django.db.models import Prefetch

# from user import permissions
from .models import Book
from .serializers import BookSerializer
from author.models import Author
from book_copy.models import BookCopy
# from utils.pagination import BookResultsPagination

# Create your views here.


@extend_schema(tags=["book"])
class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.prefetch_related(
        Prefetch("author", queryset=Author.objects.all(), to_attr="authors"),
        Prefetch(
            "copies",
            queryset=BookCopy.objects.filter(status="available"),
            to_attr="available_copies_list",
        ),
    )

    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    # pagination_class = BookResultsPagination


# @extend_schema(tags=["book"])
# class
