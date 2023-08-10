from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View


# Create your views here.


def index(request):
    Products = None
    Categorye = Category.get_all_categories()
    categoryID = request.GET.get("category")
    if categoryID:
        Products = Product.get_all_products_by_categoryid(categoryID)
    else:
        Products = Product.get_all_products()

    data = {}
    data["Products"] = Products
    data["Categorye"] = Categorye
    print('you are: ', request.session.get('email'))
    # return render(request, 'orders/order.html')
    return render(request, "index.html", data)








