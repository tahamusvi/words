from django.shortcuts import render
from .models import *

def home1(request):
    words = word.objects.all()

    return render(request,'words/home.html')


def home(request,pk=0):
    max = word.objects.all().count()
    if(pk+1 > max):
        wordPk = word.objects.get(id = 1)
    else:
        wordPk = word.objects.get(id = pk+1)
    return render(request,'words/home.html',{'word':wordPk})
