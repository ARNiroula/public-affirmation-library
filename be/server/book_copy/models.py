from django.db import models

from book.models import Book


class BookCopy(models.Model):
    STATUS_CHOICES = [
        ("available", "Available"),
        ("on_loan", "On Loan"),
        ("reserved", "Reserved"),
    ]

    copy_id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="copies")
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="available"
    )
