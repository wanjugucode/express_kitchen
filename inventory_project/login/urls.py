from django.urls import path
from .views import login

from login import views
from os import name
from django.urls import path
from login.views import *

urlpatterns = [
    path('',login,name='menu_views'),

   path('', views.index, name='Home'),
   path('signup', views.signUp, name='SignUp'),
   path('login', views.login, name='Login'),
   path('token', views.send_token, name='Token'),
   path('error', views.error, name='Error'),
   path('logout', views.logoutUser, name='Logout'),
   path('verify/<slug>', views.verify, name='Token'),
   path('forgetpass', views.forgetPassword, name='ForgetPassword'),
   path('reset/<token>', views.reset, name='ResetPass'),
]

