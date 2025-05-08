from django.db.models.signals import post_save, post_update
from django.dispatch import receiver
from .models import Order, OrderLog
