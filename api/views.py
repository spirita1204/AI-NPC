from django.http import JsonResponse
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseBadRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import NPC
from .serializers import NPCSerializer
from django.apps import apps
from django.shortcuts import render

# 測試DRF
@api_view(['GET'])
def test_drf_api(request):
    return JsonResponse({"message": "Hello, world!"})

# 測試MongoDB串接
@api_view(['GET'])
def test_mongoDb_data(request):
    # 獲取 ApiConfig 類別，進而訪問資料庫
    api_config = apps.get_app_config('api') 
    
    database = api_config.database  # 獲取資料庫實例
    collection = database['npc']
    items_cursor = collection.find()  # 查詢所有項目
    # 將游標轉換為列表
    items = list(items_cursor)

    # MongoDB 中的資料包含 ObjectId，需要轉換成字符串才能正確顯示
    for item in items:
        item['_id'] = str(item['_id'])  

    return JsonResponse({"message": items})

# 測試Unreal Engine API
@api_view(['GET'])
def TEST_UE_API(request):
    return JsonResponse({"message": "Hello, world!"})

from channels.layers import get_channel_layer
def send_character_move(request):
    # 假设从请求中获取 action 和 position
    # action = request.GET.get('action')
    # position = request.GET.get('position')

    # 获取 channel layer 并向 WebSocket 组发送消息
    channel_layer = get_channel_layer()
    channel_layer.group_send(
        'game_character_move', 
        {
            'type': 'receive',
            'action': "EAT",
            'position': {'x': 100, 'y': 100},
        }
    )
    return JsonResponse({'status': 'ok', 'action': 'EAT', 'position': {'x': 100, 'y': 100}})
    
def test_socket_index(request):
    return render(request, "api/index.html")

def test_socket_room(request, room_name):
    return render(request, "api/room.html", {"room_name": room_name})