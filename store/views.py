from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category


# Create your views here.


def index(request):
    Products = Product.get_all_products()
    Categorye = Category.get_all_categories()
    data = {}
    data['Products'] = Products
    data['Categorye'] = Categorye
    # return render(request, 'orders/order.html')
    return render(request, "index.html", data)
