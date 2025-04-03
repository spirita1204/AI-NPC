"""
ASGI config for chatDemo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AI_NPC_Backend.settings')
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

from mcp_app.routing import websocket_urlpatterns

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),# 使用 get_asgi_application() 來處理 HTTP 請求
        "websocket": AllowedHostsOriginValidator(# 使用 AuthMiddlewareStack 來驗證 WebSocket 連線
            AuthMiddlewareStack(
                URLRouter(websocket_urlpatterns)# 根據 WebSocket 請求的 URL 路徑進行路由 路由規則會指向 WebSocket 消費者（consumers）
            )
        ),
    }
)