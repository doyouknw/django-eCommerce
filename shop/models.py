from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    product_category = models.CharField(max_length=30)
    logo = models.CharField(max_length=20)

class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    unit_price = models.IntegerField(default=0)
    num_of_units = models.IntegerField(default=0)
    picture = models.CharField(max_length=30)
    color = models.CharField(max_length=10)

class UserAccount(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    reg_date = models.DateField(default=datetime.date.today)
    last_login = models.DateField(default=datetime.date.today)
    block = models.BooleanField(default=True)
    
class User(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    dob = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)