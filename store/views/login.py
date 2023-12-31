from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View



# Class Based View login
class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer']= customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url= None
                    return redirect('homepage')
            else:
                error_message = 'Email or password Invalid!!'
        else:
            error_message = 'Email or password Invalid!!'
        print(email, password, customer)
        return render(request, 'login.html', {'error': error_message})

# # Functions Based View login
# def login(request):
#     if request.method == 'GET':
#         return render(request, 'login.html')
#
#     else:
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)
#         error_message = None
#         if customer:
#             flag = check_password(password, customer.password)
#             if flag:
#                 return redirect('homepage')
#             else:
#                 error_message = 'Email or password Invalid!!'
#         else:
#             error_message = 'Email or password Invalid!!'
#         print(email, password, customer)
#         return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')