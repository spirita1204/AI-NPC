from django.urls import re_path
from . import consumers

# 配置 WebSocket 路由，供前端建立 WebSocket 連接。
websocket_urlpatterns = [
    # re_path(r'ws/character_move/$', consumers.CharacterMoveConsumer.as_asgi()),
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.CharacterMoveConsumer.as_asgi()),
]
