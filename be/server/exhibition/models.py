from django.db import models

from event.models import Event


# Create your models here.
class Exhibition(Event):
    expenses = models.DecimalField(max_digits=9, decimal_places=2)
    users = models.ManyToManyField("user.User", related_name="exhibition")

    class Meta:  # pyright: ignore
        db_table = "AYT_EXHIBITION"

    def __str__(self):
        return f"Exhibition {self.event_name}"
