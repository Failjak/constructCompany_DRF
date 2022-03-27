from django.db import models
from djmoney.models.fields import MoneyField
from django_enum_choices.fields import EnumChoiceField

from apps.types import OrderStatus


class Order(models.Model):
    title = models.CharField(max_length=255)
    status = EnumChoiceField(
        OrderStatus,
        default=OrderStatus.NOT_READY
    )
    description = models.TextField()
    budget = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

