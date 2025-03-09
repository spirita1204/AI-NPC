from django.http import JsonResponse
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseBadRequest
from rest_framework.decorators import api_view

@api_view(['GET'])
def TEST_DRF_API(request):
    return JsonResponse({"message": "Hello, world!"})

@api_view(['GET'])
def TEST_GET_MONGO_DB_DATA(request):
    return JsonResponse({"message": "Hello, world!"});