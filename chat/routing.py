from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from .consumer import ChatConsumer

websocket_urlpatterns =[
   path("ws/chat/", ChatConsumer.as_asgi()),
   
]
