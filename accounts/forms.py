from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phoneNumber','firstName','lastName']


    def __init__(self, *arg,**kwargs):
        user = kwargs.pop('user')

        super(ProfileForm, self).__init__( *arg,**kwargs)
        if not user.is_staff:
            self.fields['phoneNumber'].disabled = True
            self.fields['phoneNumber'].help_text = False
            # self.fields['is_active'].disabled = True
            # self.fields['special_user'].disabled = True
            # self.fields['is_author'].disabled = True




class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    class Meta:
        model = User
        fields = ('phoneNumber', 'email', 'password1', 'password2')
