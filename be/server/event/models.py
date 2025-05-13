from datetime import datetime, timedelta

from django.db import models
from django.db.models import Q, F

from utils.enums import EventTopic


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=100, db_index=True, default="Test")
    start_date_time = models.DateTimeField(default=datetime.now())
    end_date_time = models.DateTimeField(default=datetime.now() + timedelta(days=10))
    image_url = models.URLField(null=True, blank=True)

    event_topic = models.CharField(
        max_length=30,
        choices=EventTopic,
        default=EventTopic.LITERATURE,
        db_index=True,
    )
    topic_bitmap = models.BigIntegerField(default=0, editable=False, db_index=True)  # pyright: ignore

    class Meta:
        abstract = True
        constraints = [
            models.CheckConstraint(
                name="check_datetime_order",
                check=Q(end_date_time__gt=F("start_date_time")),
            ),
        ]

    def set_topics(self, topic_codes):
        self.event_topics_bitmap = sum(
            1 << EventTopic.bit_position(code) for code in topic_codes
        )

    def get_topics(self):
        return [
            topic
            for topic in EventTopic
            if self.event_topics_bitmap & (1 << EventTopic.bit_position(topic.value))
        ]

    def has_topic(self, code):
        return bool(self.event_topics_bitmap & (1 << EventTopic.bit_position(code)))

    def __str__(self):
        return str(self.event_name)


"""
CREATE TABLE AYT_EVENT
    (
     EVENT_ID        NUMBER (10)  NOT NULL ,
     EVENT_NAME      VARCHAR2 (100)  NOT NULL ,
     START_DATE_TIME DATE  NOT NULL ,
     END_DATE_TIME   DATE  NOT NULL ,
     EVENT_TOPIC     VARCHAR2 (30)  NOT NULL ,
     EVENT_TYPE      VARCHAR2 (1)  NOT NULL
    )
;
"""
