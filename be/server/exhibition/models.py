from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator

from event.models import Event


# Create your models here.
class Exhibition(Event):
    expenses = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("1"))],
    )
    users = models.ManyToManyField("user.User", related_name="exhibition", blank=True)

    class Meta:  # pyright: ignore
        db_table = "AYT_EXHIBITION"

    def __str__(self):
        return f"Exhibition {self.event_name}"
