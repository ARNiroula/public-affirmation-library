from django.db import models

class Sponser(models.Model):
    sponser_id = models.IntegerField(max_legth=5, primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=254)

    class Meta:
        db_table = "AYT_SPONSER"

    def __str__(self):
        return self.name