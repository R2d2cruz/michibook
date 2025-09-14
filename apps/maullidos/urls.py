from django.contrib import admin
from django.urls import path
from .views import feed, reactMaullido

urlpatterns = [
    path('', feed, name= 'feed'),
    path('reactMaullido/<int:maullido_id>', reactMaullido, name="reactMaullido")
]