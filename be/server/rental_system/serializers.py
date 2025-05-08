from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Rental


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = "__all__"
        extra_kwargs = {"actual_date": {"required": False}}
