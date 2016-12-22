from .models import LoginUser
from django.shortcuts import Http404, get_object_or_404
from django.contrib.auth.hashers import check_password, make_password
# from django.contrib.auth.models import check_password

class UserBackend:
	def authenticate(self, username = None, password = None):
		try:
			user = LoginUser.objects.get(username = username)
			test = check_password(password,user.password)
			if test:
				return user
		except LoginUser.DoesNotExist:
			print("Failed")
			return None
		
	def get_user(self,user_id):
		try:
			return LoginUser.objects.get(pk=user_id)
		except LoginUser.DoesNotExist as e:
			raise e