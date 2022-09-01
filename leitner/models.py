from django.db import models
from words.models import word
from django.utils import timezone
from datetime import timedelta
#-----------------------------------------------------------------
class Leitner(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.user.__str__() + " - " + self.title

    def search(self,text):
        for word in self.lword.all():
            if(str(text) == word.words.text):
                return True
        return False
#-----------------------------------------------------------------
class Lword(models.Model):
    status_word = (
        ('1','d1'),
        ('2','d2'),
        ('3','d3'),
        ('4','w1'),
        ('5','w2'),
        ('6','m1'),
        ('7','m2'),
    )
    words = models.ForeignKey(word, on_delete=models.CASCADE,related_name="Lword")
    cycle = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1,choices = status_word,default='1')
    leitner = models.ForeignKey(Leitner, on_delete=models.CASCADE,related_name="lword")



    def learn(self):
        if self.cycle > timezone.now():
            return False
        else:
            return True

    def condition(self,days,delta):
        if( delta >= timedelta(days=days)):
            return True
        else:
            return False

    def reviewTime(self):
        delta = timezone.now() - self.cycle

        if self.status == '1':
            return self.condition(int(self.status),delta)

        elif self.status == '2':
            return self.condition(int(self.status),delta)

        elif self.status == '3':
            return self.condition(int(self.status),delta)

        elif self.status == '4':
            return self.condition(7,delta)

        elif self.status == '5':
            return self.condition(14,delta)

        elif self.status == '6':
            return self.condition(30,delta)

        elif self.status == '7':
            return self.condition(60,delta)



    def __str__(self):
        return self.words.text


    def UpLevel(self):
        self.status = str(int(self.status)+1)
        self.cycle = timezone.now()

    def DownLevel(self):
        self.status = str(1)
        self.cycle = timezone.now()

    def learned(self):
        self.cycle = timezone.now

    learn.boolean = True
    reviewTime.boolean = True


#-----------------------------------------------------------------
