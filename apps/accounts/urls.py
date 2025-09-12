from django.contrib import admin
from django.urls import path
from .views import singin, singup

urlpatterns = [
    path('login/', singin, name="login"),
    path('registrar/', singup, name="register")
]