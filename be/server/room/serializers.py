from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Room, Booking


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"
        # extra_kwargs = {
        #     "image_url": {"write_only": True},
        # }


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
        except (Exception, ValidationError) as e:
            raise serializers.ValidationError(
                {
                    "message": e.messages  # pyright: ignore
                }
            )
        return super().validate(attrs)
