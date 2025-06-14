from django.db import models

from invoice.models import Invoice
from pay_type.models import PayType

class Pay(models.Model):
    pay_id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    class Meta:
        db_table = 'AYT_PAY'

    def __str__(self):
        return f"Payment {self.pay_id} - Amount: ${self.amount}"

class TypePayRelationship(models.Model):
    pay = models.ForeignKey(Pay, on_delete=models.CASCADE, related_name='type_pay_relationships')
    pay_type = models.ForeignKey(PayType, on_delete=models.CASCADE, related_name='type_pay_relationships')

    class Meta:
        db_table = 'AYT_TYPE_PAY_RELATIONSHIP'

    def __str__(self):
        return f"Pay {self.pay.pay_id} - Type {self.pay_type.type_id}"

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