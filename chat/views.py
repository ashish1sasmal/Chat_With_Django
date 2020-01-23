from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import ChatForm
from .models import Message
from django.contrib import messages

def home(request):
    return render(request,"chat/index.html")

def message(request,id):
    if request.method=="POST":
        form=ChatForm(data=request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.sender=request.user
            form.reciever=User.objects.get(id=id)
            form.save()
            messages.success(request,'message has been submitted!')
    form=ChatForm()
    chats=Message.objects.filter(sender=request.user,reciever=User.objects.get(id=id))
    return render(request,'chat/chat.html',{'form':form,'chats':chats})
