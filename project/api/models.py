from django.db import models

# Create your models here.


class Info(models.Model):
    id = models.Field(primary_key=True)
    weather = models.CharField(max_length=156)
    description = models.CharField(max_length=156)
    icon = models.CharField(max_length=24)
    temperature = models.CharField(max_length=24)
    feels_like = models.CharField(max_length=24)
    temp_min = models.CharField(max_length=24)
    temp_max = models.CharField(max_length=24)
    humidity = models.CharField(max_length=24)
    country = models.CharField(max_length=156)
    name = models.CharField(max_length=156)
