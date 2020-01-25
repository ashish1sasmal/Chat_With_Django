from django.urls import path
from . import views
app_name="chat"
urlpatterns = [
    path('',views.home,name='home'),
    path('message/<int:id>',views.message,name='message'),
    path('chat/<int:id>',views.chat,name='chat'),
]
