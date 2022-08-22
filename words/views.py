from django.shortcuts import render
from .models import *
import random

def home1(request):
    words = word.objects.all()

    return render(request,'words/home.html')


def home(request,pk=0):
    max = word.objects.all().count()
    learned = word.objects.filter(learn=False).count()

    QueryWord = word.objects.get(id = 1)


    while((QueryWord.learn != False) and (learned!=1)):
        pk2 = random.randrange(1,max)
        QueryWord = word.objects.get(id = pk2)



    if(learned==1):
        QueryWord = word(text = "END!",meaning="cool!",id=1000)


    return render(request,'words/home.html',{'word':QueryWord})



def changeLearnCondition(request,pk):
    QueryWord = word.objects.get(id=pk)
    QueryWord.learn = True
    QueryWord.save()

    return home(request,pk)
