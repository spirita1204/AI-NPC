from django.http import JsonResponse
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseBadRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import NPC
from .serializers import NPCSerializer
from django.apps import apps

# 測試DRF
@api_view(['GET'])
def TEST_DRF_API(request):
    return JsonResponse({"message": "Hello, world!"})

# 測試MongoDB串接
@api_view(['GET'])
def TEST_GET_MONGO_DB_DATA(request):
    # 獲取 ApiConfig 類別，進而訪問資料庫
    api_config = apps.get_app_config('api') 
    
    database = api_config.database  # 獲取資料庫實例
    collection = database['npc']
    items_cursor = collection.find()  # 查詢所有項目
     # 將游標轉換為列表
    items = list(items_cursor)

    # 注意：如果 MongoDB 中的資料包含 ObjectId，可能需要轉換成字符串才能正確顯示
    for item in items:
        item['_id'] = str(item['_id'])  # 將 _id 轉換成字符串

    return JsonResponse({"message": items})

# 測試Unreal Engine API
@api_view(['GET'])
def TEST_UE_API(request):
    return JsonResponse({"message": "Hello, world!"})