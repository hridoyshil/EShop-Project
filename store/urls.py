from os import path
from django.urls import path

from .views import home, login
from .views.signup import Signup

urlpatterns = [
    path('', home.Index.as_view(), name='homepage'),
    path('login', login.Login.as_view(), name='login'),
    path('signup', Signup.as_view(), name='signup'),
]
