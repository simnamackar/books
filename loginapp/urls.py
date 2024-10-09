from django.contrib import admin
from django.urls import path,include
from userapp.views import listview
from . import views


urlpatterns = [
path("",views.userregistration,name='register'),
path("listview/",listview,name='viewbook'),
path("login/",views.loginpage,name='login'),
path("logout/",views.logoutview,name='logout')
]