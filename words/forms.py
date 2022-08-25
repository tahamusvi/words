from django import forms
from .models import *

class GpForm(forms.ModelForm):
    class Meta:
        model = group
        fields = ['title', 'img']


class WordForm(forms.ModelForm):
    class Meta:
        model = word
        fields = ['text', 'meaning']
