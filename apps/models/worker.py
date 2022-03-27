from django.db import models


class Worker(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    experience = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)

