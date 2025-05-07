from datetime import timedelta

from django.db import models
from django.db.models import CheckConstraint, Q, F
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

"""
CREATE TABLE AYT_ROOM
    (
     ROOM_ID  VARCHAR2 (4)  NOT NULL ,
     CAPACITY NUMBER (1)  NOT NULL ,
     DESCR    VARCHAR2 (100)  NOT NULL
    )
;
"""


class Room(models.Model):
    room_id = models.CharField(max_length=4, primary_key=True)
    capacity = models.PositiveIntegerField(default=1)  # pyright: ignore
    descr = models.CharField(max_length=100)

    class Meta:
        db_table = "AYT_ROOM"


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    num_of_people = models.PositiveIntegerField(
        default=1,  # pyright: ignore
        validators=[MinValueValidator(1), MaxValueValidator(20)],
    )
    description = models.TextField(max_length=100)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    class Meta:
        db_table = "AYT_BOOKING"
        ordering = ["room", "start_datetime"]
        unique_together = [
            ["room", "start_datetime"],
        ]
        constraints = [
            CheckConstraint(
                check=Q(end_datetime__gt=F("start_datetime")),
                name="check_start_datetime",
            ),
        ]

    def clean(self):
        super().clean()

        # Number of People Must be not be greater than room capacity
        if self.num_of_people > self.room.capacity:  # pyright: ignore
            raise ValidationError("Number of People Cannot Exceed Capacity of the room")

        if self.start_datetime.date() != self.end_datetime.date():  # pyright: ignore
            raise ValidationError("Booking Must Start and End on the Same Date")

        # Room Overlap Check
        overlaps = Booking.objects.filter(  # pyright: ignore
            room=self.room,
            start_datetime__lt=self.end_datetime,
            end_datetime__gt=self.start_datetime,
        ).exclude(pk=self.pk)

        # if self.pk:
        #     overlaps = overlaps.exclude(pk=self.pk)

        if overlaps.exists():
            raise ValidationError("Room is already booked for selected time")

        # 4-hour per-limit per day
        same_date_bookings = Booking.objects.filter(  # pyright: ignore
            user=self.user,
            start_datetime__date=self.start_datetime.date(),  # pyright: ignore
        ).exclude(pk=self.pk)

        # if self.pk:
        #     same_date_bookings = same_date_bookings.exclude(pk=self.pk)
        total_duration = self.end_datetime - self.start_datetime  # pyright: ignore
        for booking in same_date_bookings:
            total_duration += booking.end_datetime - booking.start_datetime

        if total_duration > timedelta(hours=4):
            raise ValidationError("Cannot Book More than 4 hours in a single day")
