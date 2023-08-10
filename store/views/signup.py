from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
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

        error_message =self.validateCustomer(customer)
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

    def validateCustomer(self,customer):
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






# def validateCustomer(customer):
#     error_message = None
#     if not customer.first_name:
#         error_message = "First Name Required!!"
#     elif len(customer.first_name) < 4:
#         error_message = 'First name must be 4 char long or more'
#
#     if not customer.last_name:
#         error_message = 'Last Name Required!!'
#     elif len(customer.last_name) < 4:
#         error_message = 'Last Name must be 4 char long or more'
#
#     if not customer.phone:
#         error_message = 'phone Required!!'
#     elif len(customer.phone) < 10:
#         error_message = 'phone number must be 10 char long or more'
#
#     elif customer.isExists():
#         error_message = 'Email Address Already Registered... '
#
#     return error_message


# def registerUser(request):
#     pastData = request.POST
#     first_name = pastData.get('firstname')
#     last_name = pastData.get('lastname')
#     phone = pastData.get('phone')
#     email = pastData.get('email')
#     password = pastData.get('password')
#
#     # validation
#     value = {
#         'first_name': first_name,
#         'last_name': last_name,
#         'phone': phone,
#         'email': email
#     }
#
#     error_message = None
#
#     customer = Customer(first_name=first_name,
#                         last_name=last_name,
#                         phone=phone,
#                         email=email,
#                         password=password)
#
#     error_message = validateCustomer(customer)
#     # saving
#     if not error_message:
#         print(first_name, last_name, password, phone, email)
#         customer.password = make_password(customer.password)
#         customer.register()
#         # return render(request, 'index.html')
#         # return redirect('http://localhost:8000')
#         return redirect('homepage')
#
#     else:
#         date = {
#             "error": error_message,
#             "values": value
#         }
#         return render(request, "signup.html", date)
#

# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'signup.html')
#     else:
#         return registerUser(request)














