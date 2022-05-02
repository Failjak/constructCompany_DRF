from django.db import models
from djmoney.models.fields import MoneyField
from django_enum_choices.fields import EnumChoiceField
from django.contrib.auth import get_user_model


from apps.types import OrderStatus

User = get_user_model()


class Order(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    status = EnumChoiceField(
        OrderStatus,
        default=OrderStatus.NOT_READY
    )
    description = models.TextField()
    budget = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')

    def __str__(self):
        return f"{self.title}, {self.customer.name} ({self.status})"
