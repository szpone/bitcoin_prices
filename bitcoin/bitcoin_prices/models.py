from django.db import models

# Create your models here.


class Prices(models.Model):
    last_price = models.IntegerField(null=True)


class CurrentPrices(models.Model):
    current_price = models.FloatField(null=True)
    created = models.DateTimeField(auto_now_add=True)
