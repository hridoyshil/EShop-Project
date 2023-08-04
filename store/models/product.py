from django.db import models
from .category import Category


class Product(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.IntegerField(default=0)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    Description = models.CharField(max_length=200, default='')
    Image = models.ImageField(upload_to='uploads/products/')
