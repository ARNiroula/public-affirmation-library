from django.contrib.auth.models import (
    AbstractUser,
)
from django.db import models


# Create your models here.
class User(AbstractUser):
    ROLE_CHOICE = [
        ("admin", "Admin"),
        ("staff", "Staff"),
        ("customer", "Customer"),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICE, default="customer")
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
