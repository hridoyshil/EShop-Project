from os import path
from django.urls import path

from .views import index

urlpatterns = [
    path('', index)
]
