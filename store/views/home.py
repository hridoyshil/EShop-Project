from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View


# Create your views here.

class Index(View):
    def post(self , request):
        productID = request.POST.get('product')
        remove= request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(productID)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(productID)
                    else:
                        cart[productID]= quantity-1
                else:
                    cart[productID] = quantity + 1
            else:
                cart[productID] = 1
        else:
            cart = {}
            cart[productID] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart']= {}

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

# def index(request):
#     Products = None
#     Categorye = Category.get_all_categories()
#     categoryID = request.GET.get("category")
#     if categoryID:
#         Products = Product.get_all_products_by_categoryid(categoryID)
#     else:
#         Products = Product.get_all_products()
#
#     data = {}
#     data["Products"] = Products
#     data["Categorye"] = Categorye
#     print('you are: ', request.session.get('email'))
#     # return render(request, 'orders/order.html')
#     return render(request, "index.html", data)
