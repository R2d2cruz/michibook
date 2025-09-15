from django.contrib import admin
from django.urls import path
from .views import signIn, signUp, signOut

urlpatterns = [
    path('login/', signIn, name="login"),
    path('registrar/', signUp, name="register"),
    path('logout/', signOut, name="logout"),
]