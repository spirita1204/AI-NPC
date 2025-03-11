"""
ASGI config for AI_NPC_Backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import api.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AI_NPC_Backend.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(), # 使用 get_asgi_application() 來處理 HTTP 請求
    "websocket": AuthMiddlewareStack( # 使用 AuthMiddlewareStack 來驗證 WebSocket 連線
        URLRouter( # 根據 WebSocket 請求的 URL 路徑進行路由 路由規則會指向 WebSocket 消費者（consumers）。
            api.routing.websocket_urlpatterns
        )
    ),
})