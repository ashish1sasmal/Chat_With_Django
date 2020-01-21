from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    user=User.objects.exclude(id=request.user.id)
    return render(request,'chat/index.html',{'user':user})
