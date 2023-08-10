from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
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


def validateCustomer(customer):
    error_message = None
    if not customer.first_name:
        error_message = "First Name Required!!"
    elif len(customer.first_name) < 4:
        error_message = 'First name must be 4 char long or more'

    if not customer.last_name:
        error_message = 'Last Name Required!!'
    elif len(customer.last_name) < 4:
        error_message = 'Last Name must be 4 char long or more'

    if not customer.phone:
        error_message = 'phone Required!!'
    elif len(customer.phone) < 10:
        error_message = 'phone number must be 10 char long or more'

    elif customer.isExists():
        error_message = 'Email Address Already Registered... '

    return error_message


def registerUser(request):
    pastData = request.POST
    first_name = pastData.get('firstname')
    last_name = pastData.get('lastname')
    phone = pastData.get('phone')
    email = pastData.get('email')
    password = pastData.get('password')

    # validation
    value = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'email': email
    }

    error_message = None

    customer = Customer(first_name=first_name,
                        last_name=last_name,
                        phone=phone,
                        email=email,
                        password=password)

    error_message = validateCustomer(customer)
    # saving
    if not error_message:
        print(first_name, last_name, password, phone, email)
        customer.password = make_password(customer.password)
        customer.register()
        # return render(request, 'index.html')
        # return redirect('http://localhost:8000')
        return redirect('homepage')

    else:
        date = {
            "error": error_message,
            "values": value
        }
        return render(request, "signup.html", date)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return registerUser(request)


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')

    else:
        email= request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flaq = check_password(password, customer.password)
            if flaq:
                return redirect('homepage')
            else:
                error_message = 'Email or password Invalid!!'
        else:
           error_message = 'Email or password Invalid!!'
        print(email, password, customer)
        return render(request, 'login.html', {'error': error_message})
