from django.shortcuts import render
from .models import *
import random
from .forms import *
from django.shortcuts import redirect



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
    groups = group.objects.all().order_by("-id")
    return render(request,'words/panel.html',{'groups':groups})
#-----------------------------------------------------------------
def addGroup(request):
    if request.method == 'POST':
        form = GpForm(request.POST, request.FILES)

        if form.is_valid():
            newgp = group(title = form.cleaned_data['title'],img = form.cleaned_data['img']).save()
            gp = group.objects.get(title=form.cleaned_data['title'])
            return redirect('words:addWord',gp.id)
    else:
        form = GpForm()
    return render(request,'words/addgp/name-pic.html',{'form':form})
#-----------------------------------------------------------------
def addWord(request,pk):
    if request.method == 'POST':
        form = WordForm(request.POST, request.FILES)

        if form.is_valid():
            newWord = word(text = form.cleaned_data['text'],meaning = form.cleaned_data['meaning'])
            gp = group.objects.get(id=pk)
            newWord.gp = gp
            newWord.save()
            return redirect('words:addWord',gp.id)
    else:
        form = WordForm()
    return render(request,'words/addgp/addWord.html',{'form':form})
#-----------------------------------------------------------------
def GpWords(request,pk):
    gp = group.objects.get(id = pk)
    wordsGP = gp.words.all()
    max = wordsGP.count()

    w_id = [w.id for w in wordsGP if w.learn()]
    learned = wordsGP.filter(id__in=w_id).count()

    items = list(wordsGP)

    Conditon = True
    while(Conditon and ((learned!=0))):
        QueryWord = random.choice(items)
        if(QueryWord.learn() == False):
            Conditon = False



    if(learned==0):
        QueryWord = word(text = "END!",meaning="cool!",id=1000,gp=gp)

    return render(request,'words/group.html',{'word':QueryWord,'gp':gp})
#-----------------------------------------------------------------
def changeLearnCondition(request,pk):
    QueryWord = word.objects.get(id=pk)
    QueryWord.learned()
    QueryWord.save()

    return GpWords(request,QueryWord.gp.id)
#-----------------------------------------------------------------
