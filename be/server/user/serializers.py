from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model


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

    def update(self, instance, validated_data):
        if "email" in validated_data:
            raise ValidationError("Email cannot be updated!")

        if "password" in validated_data:
            instance.set_password(validated_data["password"])
            instance.save()
            return instance
        return super().update(instance, validated_data)


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class CustomerRegisterSerializer(UserRegisterSerializer):
    def create(self, validated_data):
        validated_data["role"] = "customer"
        return super().create(validated_data)


class StaffRegisterSerializer(UserRegisterSerializer):
    def create(self, validated_data):
        validated_data["role"] = "staff"
        return super().create(validated_data)


# User Profile Serializers
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "date_joined",
            "password",
        )
        read_only_fields = ["date_joined", "email"]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        raise ValidationError("Create Operation isn't allowed!")
        # return super().create(validated_data)

    def update(self, instance, validated_data):
        if "email" in validated_data:
            raise ValidationError("Email cannot be updated!")

        if "password" in validated_data:
            instance.set_password(validated_data["password"])
            instance.save()
            return instance

        return super().update(instance, validated_data)


class UserLoginResponseSerializer(serializers.Serializer):
    user = UserProfileSerializer()


class UserLogoutResponseSerializer(serializers.Serializer):
    message = serializers.CharField()


class UserStatusResponseSerializer(serializers.Serializer):
    authenticated = serializers.BooleanField()


class UserPwdForgotSerializer(serializers.Serializer):
    email = serializers.EmailField()


class UserPwdResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp_code = serializers.CharField()
    new_pwd = serializers.CharField()
