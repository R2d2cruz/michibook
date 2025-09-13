from django.contrib import admin
from django.urls import path
from .views import userProfile, users

urlpatterns = [
    path('<str:username>/', userProfile, name="userProfile"),
    path('', users, name="users")
]