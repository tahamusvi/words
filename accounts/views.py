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

#----------------------------------------------------------------------------------------------
class Login(LoginView):
    template_name = "accounts/Login.html"
    def get_success_url(self):
        user = self.request.user
        return reverse_lazy('words:panel')


        # if user.is_staff or user.is_author:
        #     return reverse_lazy('account:panelHome')
        # else:
        #     return reverse_lazy('account:profile')
#----------------------------------------------------------------------------------------------
class Profile(UpdateView):
    form_class = forms.ProfileForm
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
