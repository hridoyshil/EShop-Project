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

        # validation
        error_message = None

        if not first_name:
            error_message = "First Name Required!!"
        elif len(first_name) < 4:
            error_message = 'First name must be 4 char long or more'

        if not last_name:
            error_message='Last Name Required!!'
        elif len(last_name)< 4:
            error_message= 'Last Name must be 4 char long or more'

        if not phone:
            error_message='phone Required!!'
        elif len(phone)< 10:
            error_message= 'phone number must be 10 char long or more'




        # saving
        if not error_message:
            print(first_name, last_name, password, phone, email)

            customer = Customer(first_name=first_name,
                                last_name=last_name,
                                phone=phone,
                                email=email,
                                password=password)
            customer.register()
        else:
            return render(request, "signup.html", {"error": error_message})
