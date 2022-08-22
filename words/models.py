from django.db import models


class word(models.Model):
    text = models.CharField(max_length=30)
    meaning = models.CharField(max_length=30)
    id = models.IntegerField(primary_key=True)
    learn = models.BooleanField(default=False)


    def __str__(self):
        return self.text


class group(models.Model):
    title = models.CharField(max_length=30)
    img = models.ImageField()
    words = models.ManyToManyField(word)


    def __str__(self):
        return self.title
