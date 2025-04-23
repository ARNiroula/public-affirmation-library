from django.db import models

class Room(models.Model):
    room_id = models.CharField(max_length=4, primary_key=True)
    capacity = models.IntegerField()
    descr = models.CharField(max_length=100)

    class Meta:
        db_table = 'AYT_ROOM'

    def __str__(self):
        return self.descr


"""
CREATE TABLE AYT_ROOM 
    ( 
     ROOM_ID  VARCHAR2 (4)  NOT NULL , 
     CAPACITY NUMBER (1)  NOT NULL , 
     DESCR    VARCHAR2 (100)  NOT NULL 
    ) 
;
"""