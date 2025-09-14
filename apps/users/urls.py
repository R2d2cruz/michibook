from django.contrib import admin
from django.urls import path
from .views import userProfile, users, userEditProfile

urlpatterns = [
    path('<str:username>/', userProfile, name="userProfile"),
    path('', users, name="users"),
    path('<str:username>/profile/', userEditProfile, name="userEditProfile"),
]