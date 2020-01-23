from django.urls import path
from . import views
app_name="user"
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/<int:id>/',views.user_profile,name='profile'),
    path('users/',views.all_users,name='users')
]
