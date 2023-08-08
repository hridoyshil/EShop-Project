from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category


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
    # return render(request, 'orders/order.html')
    return render(request, "index.html", data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return HttpResponse(request.POST.get('email'))
