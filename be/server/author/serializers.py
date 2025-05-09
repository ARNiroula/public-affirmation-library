from rest_framework import serializers

from .models import Author


class AuthorBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ("auth_id", "fname", "mname", "lname")
