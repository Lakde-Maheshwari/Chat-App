from django.contrib import admin
from . import views
from django.urls import path,include
urlpatterns = [
    path("",views.chat_view,name="chat"),
    path("home/",views.home_view,name="home"),

]
