from django.shortcuts import render
from .models import *
import random

def home1(request):
    return render(request,'words/home.html')

#-----------------------------------------------------------------
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

#-----------------------------------------------------------------
def panel(request):
    groups = group.objects.all()
    return render(request,'words/panel.html',{'groups':groups})
#-----------------------------------------------------------------
def GpWords(request,pk):
    gp = group.objects.get(id = pk)
    wordsGP = gp.words.all()
    max = wordsGP.count()
    learned = wordsGP.filter(learn=False).count()

    Conditon = True
    while(Conditon and ((learned!=0))):
        QueryWord = wordsGP.get(id = random.randrange(1,max+1))
        if(QueryWord.learn == False):
            Conditon = False



    if(learned==1):
        QueryWord = word(text = "END!",meaning="cool!",id=1000,gp=gp)

    return render(request,'words/home.html',{'word':QueryWord})
#-----------------------------------------------------------------
def changeLearnCondition(request,pk):
    QueryWord = word.objects.get(id=pk)
    QueryWord.learn = True
    QueryWord.save()

    return GpWords(request,QueryWord.gp.id)
#-----------------------------------------------------------------
