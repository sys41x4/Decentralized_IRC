"""
ASGI config for Decentralized_IRC project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""
import os

from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
import websocket.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Decentralized_IRC.settings')

asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
  "http": asgi_app,
  "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                websocket.routing.websocket_urlpatterns
            )
        )
    ),
})
