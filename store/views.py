from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer


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
        pastData = request.POST
        first_name = pastData.get('firstname')
        last_name = pastData.get('lastname')
        phone = pastData.get('phone')
        email = pastData.get('email')
        password = pastData.get('password')
        print(first_name, last_name, password, phone, email)

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        customer.register()
        return HttpResponse('Signup Success')
