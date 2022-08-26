"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from home.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_asgi_application()
django_asgi_app = get_asgi_application()

# ws_patterns = [
#     path("ws/test/", TestConsumer.as_asgi() ),
#     # path("ws/chat/", ChatConsumer.as_asgi()),
# ] 

# application = ProtocolTypeRouter({
#     'websocket' : URLRouter(ws_patterns)
# })


import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator


from . import routing

application = ProtocolTypeRouter({
  "http": django_asgi_app,
  "websocket": 
        AuthMiddlewareStack(
            URLRouter(
                routing.websocket_urlpatterns
            )
        )
    
})
# application = ProtocolTypeRouter({
#     'websocket' : URLRouter(routing.websocket_urlpatterns)
# })


# application = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             ws_patterns
#         )
#     ),
# })