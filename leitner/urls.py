from django.urls import path
from .views import *




app_name = "leitner"

urlpatterns = [
    path('test/', test,name="test"),
    path('addLword/<int:id>/', addLword,name="addLword"),
    path('ReviewLeitner/', ReviewLeitner,name="ReviewLeitner"),
    path('WordLearned/<int:id>/',WordLearned,name="WordLearned"),
    path('WordUnLearned/<int:id>/',WordUnLearned,name="WordUnLearned"),
]
