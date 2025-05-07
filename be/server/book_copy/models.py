from django.db import models

from book.models import Book

class BookCopy(models.Model):
    copy_id = models.CharField(max_length=8, primary_key=True)
    book = models.ForeignKey('book.Book', on_delete=models.CASCADE, related_name='copies')