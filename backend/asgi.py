"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""


import os
from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from notification.consumers import NotificationConsumer
from notification.routing import websocket_urlpatterns
from chat.routing import websocket_urlpatterns as chat_websocket_urlpatterns


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": application,
    "websocket":URLRouter(websocket_urlpatterns + chat_websocket_urlpatterns) 
        
    
})
