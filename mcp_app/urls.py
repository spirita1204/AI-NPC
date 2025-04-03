from django.urls import path
from . import views

urlpatterns = [
    # socket
    path("chat/index",              views.test_socket_index, name="index"),
    path("chat/<str:room_name>/",   views.test_socket_room,  name="room"),
]