from django.db import models

# Create your models here.
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    friends=models.ManyToManyField(User,related_name='friends',blank=True)
    ip=models.CharField(max_length=40,default='localhost')
    isp=models.CharField(max_length=70,default='default')
    state=models.CharField(max_length=40,default='default')
    country=models.CharField(max_length=40,default='default')
    last_login=models.DateTimeField(default=datetime.now, blank=True)
    last_modified=models.DateTimeField(default=datetime.now, blank=True)
    zip=models.CharField(max_length=6,default='default' )

    def __str__(self):
    	return f'{self.user.username} Profile'
