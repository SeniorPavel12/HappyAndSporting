"""
ASGI config for HaSpo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HaSpo.settings")
import django
django.setup()
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from django_channels_jwt_auth_middleware.auth import JWTAuthMiddleware

from workout.wb.consumer import RunWorkoutConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HaSpo.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": JWTAuthMiddleware(
        URLRouter(
            [
                path('ws/run_workout/', RunWorkoutConsumer.as_asgi())
            ]
        )
    ),
})
