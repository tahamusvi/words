from django.db import models
from django.utils import timezone

class group(models.Model):
    title = models.CharField(max_length=30)
    img = models.ImageField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)


    def __str__(self):
        return self.title

    def getId(self):
        return self.id


class word(models.Model):
    text = models.CharField(max_length=30)
    meaning = models.CharField(max_length=30)
    id = models.IntegerField(primary_key=True)
    gp = models.ForeignKey(group, on_delete=models.CASCADE,related_name="words")
    # cycle = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.text

    # def learn(self):
    #     if self.cycle > timezone.now():
    #         return False
    #     else:
    #         return True

    # def learned(self):
    #     self.cycle = timezone.now


    # learn.boolean = True
