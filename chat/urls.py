from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('message/<int:id>',views.message,name='message'),
]
