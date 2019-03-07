from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(forms.Form):
  Signature = forms.CharField(label='Signature', max_length=200)
  Avatar = forms.ImageField(label='Avatar', help_text='max 42MB', required=False)
  class Meta:
    model = UserProfile
    fields = ('Signature', 'Avatar')


class SignUpForm(UserCreationForm):
  first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
  last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
  email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

  class Meta:
      model = User
      fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
