from django.contrib import admin
from .models import *
from django.contrib import admin


class WordAdmin(admin.ModelAdmin):
    list_display = ('id','text',  'gp',)
    list_editable = ( 'gp',)














admin.site.register(word,WordAdmin)
admin.site.register(group)
