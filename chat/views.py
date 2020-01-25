from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from .forms import ChatForm
from .models import Message
from django.http import HttpResponse
from django.contrib import messages
def home(request):
    return render(request,"chat/index.html")

def message(request,id):

    return HttpResponse("")


def chat(request,id):
    if request.method=="POST":
        print("here!")
        print(request.POST)
        pl=request.POST
        form=Message(sender=request.user, reciever=User.objects.get(id=id),text=request.POST.get('messa'))
        form.save()
        print('sav')
        messages.success(request,'message has been submitted!')
    chats=(Message.objects.filter(sender=request.user, reciever=User.objects.get(id=id))|Message.objects.filter(reciever=request.user, sender=User.objects.get(id=id))).order_by('timestamp')
    return render(request,'chat/chat.html',{'chats':chats,'id':id})
