from os import path
from django.urls import path

from .views import home, login
from .views.signup import Signup
from .views.login import logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('login', login.Login.as_view(), name='login'),
    path('signup', Signup.as_view(), name='signup'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders',auth_middleware(OrderView.as_view()), name='orders'),
    

]
