from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.forms.widgets import TextInput, PasswordInput
from django.urls import reverse

# user registration form
class UserRegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address', 'password1', 'password2',]


# user login form
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)


# user update form
class UserUpdateForm(UserChangeForm):
    userPic = forms.ImageField(required=False)
    phone = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'address', 'userPic',]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password', None)  # Removes the password field


# feedback form
class FeedbackForm(forms.ModelForm):
    
    class Meta:
        model = UserFeedbacks
        fields = ['title', 'association', 'description',]
        exclude = ['user',]


