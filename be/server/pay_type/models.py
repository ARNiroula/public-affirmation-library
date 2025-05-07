from django.db import models

from pay.models import Pay
from pay_type import PayTypeManager

class PayType(models.Model):
    type_id = models.ForeignKey(PayTypeManager, on_delete=models.CASCADE, null=True, blank=True)
    pay_id = models.ForeignKey(Pay, on_delete=models.CASCADE, null=True, blank=True)
    type_name = models.CharField(max_length=20)
    descr = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        db_table = 'AYT_PAY_TYPE'

    def __str__(self):
        return self.type_name

"""
CREATE TABLE AYT_PAY_TYPE 
    ( 
     TYPE_ID   NUMBER (1)  NOT NULL , 
     TYPE_NAME VARCHAR2 (20)  NOT NULL , 
     DESCR     VARCHAR2 (200) 
    ) 
;
"""