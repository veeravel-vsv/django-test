from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class LoginUser(AbstractBaseUser):
	username = models.CharField(max_length = 200, unique = True)
	password = models.CharField(max_length = 200)
	is_active = models.BooleanField(default = True)	
	is_admin = models.BooleanField(default = True)
	

	REQUIRED_FIELDS = ['password']

	USERNAME_FIELD = 'username'

	@property
	def is_staff(self):
		return self.is_admin

	@property
	def is_superuser(self):
		return True

	def get_short_name(self):
		return self.username

	def has_perm(self, perm, obj = None):
		return self.is_admin

	def has_module_perms(self,app_label):
		return self.is_admin