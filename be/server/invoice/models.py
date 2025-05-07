from django.db import models
from rental_system.models import Rental

class Invoice(models.Model):
    invoice_id = models.BigIntegerField(primary_key=True)
    invoice_date = models.DateField()
    total_amount = models.DecimalField(max_digits=6, decimal_places=2)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)

    class Meta:
        db_table = 'AYT_INVOICE'

    def __str__(self):
        return f"Invoice {self.invoice_id} - Amount: ${self.total_amount}"
     

"""
CREATE TABLE AYT_INVOICE 
    ( 
     INVOICE_ID   NUMBER (8)  NOT NULL , 
     INVOICE_DATE DATE  NOT NULL , 
     TOTAL_AMOUNT NUMBER (6,2)  NOT NULL , 
     RENTAL_ID    NUMBER (10)  NOT NULL 
    ) 
;
"""
