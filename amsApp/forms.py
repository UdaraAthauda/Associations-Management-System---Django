from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address', 'password1', 'password2',]