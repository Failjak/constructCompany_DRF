from django.db import models
from djmoney.models.fields import MoneyField


class Material(models.Model):
    name = models.CharField(max_length=255)
    weight = models.PositiveIntegerField(blank=True, null=True)
    count = models.PositiveIntegerField(blank=True, null=True)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')