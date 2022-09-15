from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from . import forms
from django.contrib.auth.views import LoginView
from django.views.generic import (
            ListView,
            CreateView,
            UpdateView,
            DeleteView,
            DetailView,)
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render,redirect
from .forms import *
from  django.contrib.auth import authenticate
from  django.contrib.auth import logout as lgo
from  django.contrib.auth import login as lg
from django.contrib import messages
from .models import User

#----------------------------------------------------------------------------------------------
def Login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        print("ok")
        if form.is_valid():
            print("ok2")
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                lg(request,user)
                messages.success(request,'you logged in successfully','success')
                return redirect('words:panel')
            else:
                messages.error(request,'username or password is wrong','alert')
    else:
        form = UserLoginForm
    return render(request,"accounts/Login.html",{'form':form})


#----------------------------------------------------------------------------------------------
class Profile(UpdateView):
    form_class = ProfileForm
    template_name = "accounts/Profile.html"
    model = User
    success_url = reverse_lazy('words:home')

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user' : self.request.user
        })
        return kwargs
#----------------------------------------------------------------------------------------------
class PasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('account:password_change_done')
