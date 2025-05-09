from django.db import models

from seminar.models import Seminar


class Sponser(models.Model):
    sponser_id = models.AutoField(max_length=5, primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=254)

    class Meta:
        db_table = "AYT_SPONSER"

    def __str__(self):
        return self.name


class SponserSeminarRelationship(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    sponser = models.ForeignKey(Sponser, on_delete=models.CASCADE)
    seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE)

    class Meta:
        db_table = "AYT_SPONSER_SEMINAR_RELATIONSHIP"


# number datatype is IntegerField.

