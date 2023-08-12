from django.db import models
from .category import Category


class Product(models.Model):
    Name = models.CharField(max_length=50)
    Price = models.IntegerField(default=0)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    Description = models.CharField(max_length=200, default='', null=True, blank=True)
    Image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(Category=category_id)
        else:
            return Product.get_all_products();
