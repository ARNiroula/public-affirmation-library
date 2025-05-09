from django.db import models

# from book.models import Book
from seminar.models import Seminar


class Author(models.Model):
    auth_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30)
    mname = models.CharField(max_length=10, blank=True, null=True)
    lname = models.CharField(max_length=30, blank=True, null=True)
    addr_st = models.CharField(max_length=100, blank=True, null=True)
    addr_city = models.CharField(max_length=100, blank=True, null=True)
    addr_state = models.CharField(max_length=100, blank=True, null=True)
    addr_ctry = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)

    class Meta:
        db_table = "AYT_AUTHOR"

    def __str__(self):
        name = self.fname
        if self.mname is not None:
            name += f" {self.mname}"
        if self.lname is not None:
            name += f" {self.lname}"
        return f"{name}"


class AuthorBookRelationship(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.ForeignKey("book.Book", on_delete=models.CASCADE)
    role = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        unique_together = ("author", "book")


class AuthorSeminarRelationship(models.Model):
    invitation_id = models.CharField(max_length=10, primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE)


"""
CREATE TABLE AYT_AUTHOR
    (
     AUTH_ID    INT  NOT NULL ,
     FNAME      VARCHAR (30)  NOT NULL ,
     MNAME      VARCHAR (10) ,
     LNAME      VARCHAR (30) ,
     ADDR_ST    VARCHAR (100) ,
     ADDR_CITY  VARCHAR (100) ,
     ADDR_STATE VARCHAR (100) ,
     ADDR_CTRY  VARCHAR (100) ,
     EMAIL      VARCHAR (254)
    )
;
"""
