from django.contrib import admin
from django.urls import path
from .views import signIn, signUp

urlpatterns = [
    path('login/', signIn, name="login"),
    path('registrar/', signUp, name="register")
]