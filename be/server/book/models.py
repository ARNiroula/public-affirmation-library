from django.db import models


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=13)
    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=50)
    summary = models.CharField(max_length=50, default="Lorem Ipsum")
    pub_date = models.DateTimeField()
    cover_url = models.URLField(null=True, blank=True)

    class Meta:
        db_table = "AYT_BOOK"


"""
CREATE TABLE AYT_BOOK
    (
     BOOK_ID  INT  NOT NULL ,
     ISBN     VARCHAR (13)  NOT NULL ,
     NAME     VARCHAR (200)  NOT NULL ,
     TOPIC    VARCHAR (50)  NOT NULL ,
     PUB_DATE TIMESTAMP(0)  NOT NULL
    )
;
"""
