from django.contrib import admin
from .models import (Category, Product)
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = Category
class ProductAdmin(admin.ModelAdmin):
    class Meta:
        model = Product

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)