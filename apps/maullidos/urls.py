from django.contrib import admin
from django.urls import path
from .views import feed, createMaullido

urlpatterns = [
    path('', feed, name= 'feed'),
    path('maullidoCreate', createMaullido, name="userMaullidoCreate"),
]