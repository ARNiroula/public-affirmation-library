from rest_framework import serializers

from .models import Rental


class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = "__all__"

        extra_kwargs = {"actual_date": {"required": False}}


class RentalRequestSerializer(serializers.Serializer):
    book_ids = serializers.ListField(child=serializers.IntegerField(min_value=0))


class RentalResponseSerializer(serializers.Serializer):
    rentals = RentalSerializer(many=True)
