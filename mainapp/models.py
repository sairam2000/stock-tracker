from django.db import models

class Channel(models.Model):
    channel_name = models.CharField(max_length=255, unique=True)

class StockDetail(models.Model):
    stock = models.CharField(max_length=255, unique=True)
    channel = models.ManyToManyField(Channel)