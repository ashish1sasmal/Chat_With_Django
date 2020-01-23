from django.db import models
from user.models import Profile
from datetime import datetime
from django.contrib.auth.models import User

class Message(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name="sender",unique=False)
    reciever=models.ForeignKey(User,on_delete=models.CASCADE,related_name="reciever",unique=False)
    text=models.CharField(max_length=1000)
    timestamp=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.sender.first_name} Message'
