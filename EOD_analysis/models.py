from django.db import models

# Create your models here.
class Stocks(models.Model):
    symbol=models.CharField(max_length=50)
    company=models.CharField(max_length=100)

class EOD_bullish_stocks(models.Model):
    date=models.DateField()
    symbol=models.CharField(max_length=50)
    strategy=models.CharField(max_length=100)

class EOD_bearish_stocks(models.Model):
    date=models.DateField()
    symbol=models.CharField(max_length=50)
    strategy=models.CharField(max_length=100)

