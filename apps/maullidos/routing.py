from django.urls import re_path
from .consumers import MaullidoConsumer

websocket_urlpatterns = [
    re_path(r"ws/maullidos/$", MaullidoConsumer.as_asgi()),
]
