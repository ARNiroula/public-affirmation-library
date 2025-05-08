from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    available_copies = serializers.SerializerMethodField()
    topic_display = serializers.CharField(source="get_topic_display", read_only=True)

    class Meta:
        model = Book
        fields = "__all__"

    def get_available_copies(self, obj):
        return obj.copies.filter(status="available").count()
