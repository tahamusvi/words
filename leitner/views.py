from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from words.models import *
import random

def test(request):
    l = Leitner.objects.get(id=1)
    lword = l.lword.get(id=2)
    # f = lword.status
    # lword.UpLevel()
    # lword.save()

    return HttpResponse(lword.cycle.day)


def addLword(request,id):
    w = word.objects.get(id=id)
    lw = Lword(words = w,status='1',leitner=request.user.leitner).save()

    return HttpResponse(lw)


#-----------------------------------------------------------------
def ReviewLeitner(request):
    lws = request.user.leitner.lword.all()

    w_id = [w.id for w in lws if w.reviewTime()]

    items = list(lws.filter(id__in=w_id))

    try:
        QueryWord = random.choice(items)
    except IndexError :
        QueryWord = None




    return render(request,'leitner/lw.html',{'QueryWord':QueryWord})
#-----------------------------------------------------------------
def WordLearned(request,id):
    lw = request.user.leitner.lword.get(id=id)
    lw.UpLevel()
    lw.save()

    return ReviewLeitner(request)
#-----------------------------------------------------------------
def WordUnLearned(request,id):
    lw = request.user.leitner.lword.get(id=id)
    lw.DownLevel()
    lw.save()

    return ReviewLeitner(request)
