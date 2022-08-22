from django.urls import path
from .views import *




app_name = "words"

urlpatterns = [
    path('', home,name="home"),
    path('words/<int:pk>', home,name="home2"),
]
