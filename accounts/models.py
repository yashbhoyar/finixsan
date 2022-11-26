from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Create your models here.
class Stocks(models.Model):
    id=models.AutoField(primary_key=True)
    symbol=models.CharField(max_length=50)
    company=models.CharField(max_length=100)

class EOD_prices(models.Model):
    id=models.AutoField(primary_key=True)
    stock_id=models.ForeignKey(Stocks,on_delete=models.CASCADE)
    open=models.FloatField()
    high=models.FloatField()
    low=models.FloatField()
    close=models.FloatField()
    volume=models.FloatField()
    date=models.DateField()

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to="profile_pictures/")

    def __str__(self):
        return f" {self.user.username}"