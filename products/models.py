from django.db import models
import datetime
# Create your models here.
class Category(models.Model):
    product_category = models.CharField(max_length=30)
    logo = models.CharField(max_length=20)
    def __str__(self):
        return self.product_category

class Product(models.Model):
    product_name = models.CharField(max_length=30)
    product_cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    unit_price = models.IntegerField(default=0)
    num_of_units = models.IntegerField(default=0)
    picture = models.CharField(max_length=30)
    color = models.CharField(max_length=10)
    def __str__(self):
        return self.product_name