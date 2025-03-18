from django.urls import path
from . import views

urlpatterns = [
    path('test_drf_api/',           views.test_drf_api),
    path('test_mongoDb_data/',      views.test_mongoDb_data),
    path('send_move/',              views.send_character_move),
    # socket
    path("chat/index",              views.test_socket_index, name="index"),
    path("chat/<str:room_name>/",   views.test_socket_room,  name="room"),
]