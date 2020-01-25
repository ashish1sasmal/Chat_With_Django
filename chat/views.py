from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from .forms import ChatForm
from .models import Message
from django.http import HttpResponse
from django.contrib import messages
def home(request):
    return render(request,"chat/index.html")

def message(request,id):
    print("here!")
    print(request.POST)
    if request.POST.get('message')!='':
        form=Message(sender=request.user, reciever=User.objects.get(id=id),text=request.POST.get('message'))
        form.save()
        print('sav')
        messages.success(request,'message has been submitted!')
    return HttpResponse("")


def chat(request,id):

    chats=(Message.objects.filter(sender=request.user, reciever=User.objects.get(id=id))|Message.objects.filter(reciever=request.user, sender=User.objects.get(id=id))).order_by('timestamp')
    return render(request,'chat/chat.html',{'chats':chats,'id':id})
