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
    form=UserForm()
    if request.method=="POST":
        form=UserForm(data=request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            ip=request.META.get('REMOTE_ADDR')
            print(ip)
            user.username=form.cleaned_data['email']
            # url="http://ip-api.com/json/"+str(ip)
            # r=get(url)
            # r=r.json()
            # print(r)
            # state=r['city']
            # country=r['country']
            # zip=r['zip']
            # isp=r['as']
            user.save()
            profile=Profile(user=user,ip='ip',zip='zip',state='state',country='country',isp='isp')
            profile.save()

            messages.success(request,"Your account has been created")
            return redirect('home')
        else:
            messages.danger(request,str(form.errors))
    else:
        form=UserForm()
    return render(request,'user/signup.html',{'form':form})

def user_login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(username=email,password=password)
        if user:
            if user.is_active:
                login(request,user)
                messages.success(request, f'You are logged in successfully!')
                return redirect('home')

        else:
            messages.error(request,'Please Check your username and password !')
    return render(request,'user/login.html')
