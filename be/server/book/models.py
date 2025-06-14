from django.db import models

from utils.enums import Topic
from author.models import Author, AuthorBookRelationship


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=13, unique=True)
    name = models.CharField(max_length=200, db_index=True)

    topic = models.CharField(
        max_length=50,
        choices=Topic,
        default=Topic.FICTION,
        db_index=True,
    )

    topic_bitmap = models.BigIntegerField(default=0)  # pyright: ignore

    summary = models.CharField(max_length=50, default="Lorem Ipsum")
    pub_date = models.DateField(null=True, blank=True)
    cover_url = models.URLField(null=True, blank=True)
    author = models.ManyToManyField(
        Author, through=AuthorBookRelationship, related_name="book"
    )

    def __str__(self):
        return f"{self.name}\n[ISBN {self.isbn}]"

    class Meta:
        db_table = "AYT_BOOK"

    def set_topics(self, topic_codes):
        bitmask = 0
        for code in topic_codes:
            bitmask |= 1 << Topic.bit_position(code)
        self.topic_bitmap = bitmask

    def get_topics(self):
        return [
            topic
            for topic in Topic
            if self.topic_bitmap & (1 << Topic.bit_position(topic.value))
        ]

    def has_topic(self, code):
        return bool(self.topic_bitmap & (1 << Topic.bit_position(code)))


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

    # topic = models.CharField(
    #     max_length=50,
    #     choices=Topic,
    #     default=Topic.FICTION,
    # )
"""
