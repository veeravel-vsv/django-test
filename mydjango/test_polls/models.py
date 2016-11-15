from django.db import models
from django import forms
from django.forms import ModelForm

# Create your models here.
class LoginUser(models.Model):
	username = models.CharField(max_length = 200)
	password = models.CharField(max_length = 200)