from django.db import models

class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    borrow_date = models.DateField()
    expected_date = models.DateField()
    actual_date = models.DateField(null=True, blank=True)
    cust_id = models.IntegerField()
    copy_id = models.BigIntegerField()

    class Meta:
        db_table = 'AYT_RENTAL'

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