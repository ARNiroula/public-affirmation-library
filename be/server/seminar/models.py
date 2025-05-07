from django.db import models

from event.models import Event

class Seminar(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='seminars')
    keynote_speaker = models.CharField(max_length=100)
    seminar_type = models.CharField(max_length=50)

    class Meta:
        db_table = "AYT_SEMINAR"

    def __str__(self):
        return self.seminar_name

# Create your models here.
