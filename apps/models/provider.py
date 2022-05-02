from django.db import models

from .material import Material


class Provider(models.Model):
    name = models.CharField(max_length=255)
    materials = models.ManyToManyField(Material, related_name='provider')

    def __str__(self):
        return self.name


# class ProviderMaterial(models.Model):
#     provider = models.OneToOneField(Provider, on_delete=models.CASCADE)
#     material = models.OneToOneField(Material, on_delete=models.PROTECT)
#     count = models.PositiveIntegerField(max_length=5)
#
#     def __str__(self):
#         return f"{self.provider} - {self.material}, {self.count}"
