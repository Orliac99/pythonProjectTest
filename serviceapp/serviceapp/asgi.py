"""
ASGI config for serviceapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_devTech.settings')

application = get_asgi_application()

# import os
#
# from django.urls import path
# from channels.auth import AuthMiddlewareStack
# from channels.security.websocket import AllowedHostsOriginValidator
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'serviceapp.settings')
#
# # import justchat.routing
# from serviceapp.justchat.consumers import ChatConsumer
#
# django_asgi_app = get_asgi_application()
#
# application = ProtocolTypeRouter({
#   "http": django_asgi_app,
#   "websocket": AllowedHostsOriginValidator(
#     AuthMiddlewareStack(
#       URLRouter(
#         path('ws/<int:id>/', ChatConsumer)
#       )
#     )
#   ),
# })