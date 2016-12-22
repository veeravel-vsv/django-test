from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import LoginUser

class LoginForm(AuthenticationForm):
	"""docstring for LoginForm"""
	username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'name': 'txtUser'}))
	password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'name': 'txtPassword'}))

	