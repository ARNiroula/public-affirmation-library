from django.db import models


class Sponser(models.Model):
    TYPE = (
        ("I", "Individual"),
        ("O", "Organization"),
    )
    sponser_id = models.AutoField(max_length=5, primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=254, unique=True)
    sponsor_type = models.CharField(max_length=1, choices=TYPE)

    class Meta:
        db_table = "AYT_SPONSER"

    def __str__(self):
        return f"{self.fname} {self.email}"


class SponserSeminarRelationship(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    sponser = models.ForeignKey(Sponser, on_delete=models.CASCADE)
    seminar = models.ForeignKey("seminar.Seminar", on_delete=models.CASCADE)

    class Meta:
        db_table = "AYT_SPONSER_SEMINAR_RELATIONSHIP"


# number datatype is IntegerField.
