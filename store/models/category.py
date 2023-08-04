from django.db import models

class Category(models.Model):
    Name= models.CharField(max_length=20)