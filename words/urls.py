from django.urls import path
from .views import *




app_name = "words"

urlpatterns = [
    path('', home,name="home"),
    path('changeLearnCondition/<int:pk>', changeLearnCondition,name="changeLearnCondition"),

]
