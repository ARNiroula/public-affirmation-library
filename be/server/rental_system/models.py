from django.db import models
from django.db.models import CheckConstraint, Q, F

from user.models import User
from book_copy.models import BookCopy


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    borrow_date = models.DateField()
    expected_date = models.DateField()
    actual_date = models.DateField(null=True, blank=True)
    cust = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rentals")
    copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE, related_name="rentals")

    class Meta:
        db_table = "AYT_RENTAL"
        unique_together = [
            ["cust", "copy", "borrow_date"],
        ]

        constraints = [
            CheckConstraint(
                check=Q(expected_date__gt=F("borrow_date")),
                name="check_borrow_date",
            )
        ]

    def __str__(self):
        return f"Rental {self.rental_id}"


"""
CREATE TABLE AYT_RENTAL
    (
     RENTAL_ID     NUMBER (10)  NOT NULL ,
     BORROW_DATE   DATE  NOT NULL ,
     EXPECTED_DATE DATE  NOT NULL ,
     ACTUAL_DATE   DATE ,
     CUST_ID       INTEGER  NOT NULL ,
     COPY_ID       NUMBER (8)  NOT NULL
    )
;
"""
