from django.db import models

from event.models import Event


class Seminar(Event):
    keynote_speaker = models.CharField(max_length=100)
    seminar_type = models.CharField(max_length=50)
    sponser = models.ManyToManyField(
        "sponser.Sponser",
        through="sponser.SponserSeminarRelationship",
        related_name="seminar",
    )

    class Meta:  # pyright: ignore
        db_table = "AYT_SEMINAR"

    def __str__(self):
        return str(self.event_name)


# Create your models here.
