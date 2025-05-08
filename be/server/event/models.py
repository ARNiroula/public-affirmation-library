from django.db import models


class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event_name = models.CharField(max_length=100)
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    event_topic = models.CharField(max_length=30)
    event_type = models.CharField(max_length=1)

    class Meta:
        db_table = "AYT_EVENT"

    def __str__(self):
        return self.event_name


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

