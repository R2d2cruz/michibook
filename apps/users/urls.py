from django.contrib import admin
from django.urls import path
from .views import userProfile, users

urlpatterns = [
    path('<int:task_id>/', userProfile, name="userProfile"),
    path('', users, name="users")
]