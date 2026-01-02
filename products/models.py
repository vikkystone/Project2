from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2083)

class Offer(models.Model):
    offer = models.FloatField()
    description = models.CharField()