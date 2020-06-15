from django.db import models


class Merchant_Details(models.Model):
    is_merchant = models.BooleanField(default=False)
    first_name = models.TextField(max_length=40)
    username = models.CharField(max_length=80)
    email = models.EmailField()
    phone = models.IntegerField()
    adhar = models.IntegerField()
    gstin = models.CharField(max_length=20)
    bank = models.IntegerField()
    acc_name = models.CharField(max_length=40)
    ifsc = models.CharField(max_length=20)