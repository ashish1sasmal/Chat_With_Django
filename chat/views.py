from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):
    return render(request,"chat/index.html")
