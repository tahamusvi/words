from django.shortcuts import render
from django.http import HttpResponse
from .models import Leitner

def test(request):
    l = Leitner.objects.get(id=1)
    lword = l.lword.get(id=2)
    # f = lword.status
    # lword.UpLevel()
    # lword.save()

    return HttpResponse(lword.cycle.day)
