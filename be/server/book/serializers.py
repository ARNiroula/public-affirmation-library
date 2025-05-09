from rest_framework import serializers

from .models import Book
from author.serializers import AuthorBookSerializer


class BookSerializer(serializers.ModelSerializer):
    available_copies = serializers.SerializerMethodField()
    topic_display = serializers.CharField(source="get_topic_display", read_only=True)
    authors = AuthorBookSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        # fields = "__all__"
        exclude = (
            "author",
            "topic_bitmap",
            "topic",
        )

    def get_available_copies(self, obj):
        return len(obj.available_copies_list)
        # return obj.copies.filter(status="available").count()
