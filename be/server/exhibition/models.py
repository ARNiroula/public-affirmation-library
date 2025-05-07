from django.db import models

from event.models import Event

class Exhibition(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='exhibitions')
    expenses = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        db_table = "AYT_EXHIBITION"

    def __str__(self):
        return self.exhibition_name

# Create your models here.
