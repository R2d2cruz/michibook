from django.contrib import admin
from django.urls import path
from .views import singin, singup

urlpatterns = [
    path('singin/', singin, name="singin"),
    path('singup/', singup, name="singup")
]