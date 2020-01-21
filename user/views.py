from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import UserForm,ProfileForm
from .models import Profile
from requests import get
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

# Create your views here.
def signup(request):
    if request

def user_login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(username=email,password=password)
        if user:
            if user.is_active:
                login(request,user)
                messages.success(request,"Successfully logged in !")
                return redirect('home')
        else:
            messages.warning(request,"Wrong email id or password!")
    return render(request,"user/login.html")

def signup(request):
    return render(request,"user/signup.html")
