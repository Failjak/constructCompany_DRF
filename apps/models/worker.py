from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=255)

    experience = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}, {self.speciality}"
