from django.urls import path
from api.views import TEST_DRF_API, TEST_GET_MONGO_DB_DATA  # 這個 view 函式目前還沒寫

urlpatterns = [
    path('TEST_DRF_API/', TEST_DRF_API),
    path('TEST_GET_MONGO_DB_DATA/', TEST_GET_MONGO_DB_DATA),
]