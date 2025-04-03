from django.shortcuts import render

# Create your views here.
def test_socket_index(request):
    return render(request, "mcp_app/index.html")

def test_socket_room(request, room_name):
    return render(request, "mcp_app/room.html", {"room_name": room_name})