from django.db import models

class Product(models.Model):
    Name= models.CharField(max_length=50)
    Price= models.IntegerField(default=0)
    Description= models.CharField(max_length=200, default='')
    Image= models.ImageField(upload_to='products/')

