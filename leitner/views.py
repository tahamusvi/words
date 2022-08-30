from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from words.models import *

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
