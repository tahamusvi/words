from django.urls import path
from .views import *




app_name = "words"

urlpatterns = [
    path('', panel,name="panel"),
    path('<int:pk>/', GpWords,name="home"),
    # path('GpWords/<int:pk>/', GpWords,name="GpWords"),
    path('changeLearnCondition/<int:pk>', changeLearnCondition,name="changeLearnCondition"),

]
