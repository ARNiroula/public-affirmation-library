from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model


# Custom JWT Token serializers
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["role"] = user.role
        token["is_staff"] = user.is_staff
        token["date_joined"] = str(user.date_joined.strftime("%Y-%m-%d"))
        return token


# User Registration serializers
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
        )
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        user.save()
        return user


class CustomerRegisterSerializer(UserRegisterSerializer):
    def create(self, validated_data):
        validated_data["role"] = "customer"
        return super().create(validated_data)


class StaffRegisterSerializer(UserRegisterSerializer):
    def create(self, validated_data):
        validated_data["role"] = "staff"
        return super().create(validated_data)
