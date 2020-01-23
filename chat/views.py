from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    
    return render(request,'chat/chat.html', {})
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

