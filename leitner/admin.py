from django.contrib import admin
from .models import *


class LwordAdmin(admin.ModelAdmin):
    list_display = ('words','cycle',  'status','leitner',  'reviewTime')
    list_editable = ( 'status','cycle')









admin.site.register(Leitner)
admin.site.register(Lword,LwordAdmin)
