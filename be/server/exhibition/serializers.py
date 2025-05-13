from rest_framework import serializers

from .models import Exhibition


class ExhibitionSerializer(serializers.ModelSerializer):
    total_registered = serializers.SerializerMethodField()

    class Meta:
        model = Exhibition
        read_only_fields = [
            "event_name",
            "start_date_time",
            "end_date_time",
            "image_url",
            "event_topic",
        ]
        exclude = (
            "topic_bitmap",
            "users",
            "expenses",
        )

    def get_total_registered(self, obj):
        return len(obj.users_list)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)

        user_data = self.context["request"].user
        if user_data is None:
            raise serializers.ValidationError(
                {"message": "Cannot Perform Action"},
            )

        instance.users.add(user_data)
        instance.save()
        return instance
