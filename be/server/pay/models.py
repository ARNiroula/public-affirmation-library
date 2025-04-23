from django.db import models

class Pay(models.Model):
    pay_id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    invoice_id = models.BigIntegerField()

    class Meta:
        db_table = 'AYT_PAY'

    def __str__(self):
        return f"Payment {self.pay_id} - Amount: ${self.amount}"

"""
CREATE TABLE AYT_PAY 
    ( 
     PAY_ID     NUMBER (10)  NOT NULL , 
     DATE_TIME  DATE  NOT NULL , 
     AMOUNT     NUMBER (6,2)  NOT NULL , 
     INVOICE_ID NUMBER (10)  NOT NULL 
    ) 
;
"""