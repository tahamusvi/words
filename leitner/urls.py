from django.urls import path
from .views import *




app_name = "leitner"

urlpatterns = [
    path('test/', test,name="test"),
]
