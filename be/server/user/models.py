from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.


# Created a CustomeUserManager to add the default role of admin
# for Super User
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("role", "admin")

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if kwargs.get("role") != "admin":
            raise ValueError("Superuser must have role=Admin.")

        return self.create_user(email, password, **kwargs)


class User(AbstractUser):
    ROLE_CHOICE = [
        ("admin", "Admin"),
        ("staff", "Staff"),
        ("customer", "Customer"),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICE, default="customer")
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    objects = CustomUserManager()
