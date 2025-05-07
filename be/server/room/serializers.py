from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Room, Booking


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        read_only_fields = ["user"]

    def validate(self, attrs):
        user = self.context["request"].user
        if not self.instance:
            attrs["user"] = user

        instance = Booking(**attrs)

        if self.instance:
            instance.pk = self.instance.pk
            attrs["user"] = user

        try:
            instance.full_clean()
        except ValidationError as e:
            raise ValidationError(str(e))

        return super().validate(attrs)
