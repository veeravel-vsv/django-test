from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import LoginUser
# Create your views here.

def login(request):
	# usr_id = get_object_or_404(LoginUser, pk = users_id)
	return render(request, 'polls/login.html')
	# return render(request, 'polls/index.html', {'a':users_id})

def index(request):
	# if request.method == "POST":
	# 	login_usr = LoginUser(request.POST)
	# 	if login_usr.is_valid():
	# 		usr_name = login_usr.cleaned_data['usrText']
	# else:
	# 	login_usr = LoginUser()
	login_usr = LoginUser(request.POST)
	return render(request, 'polls/index.html',{'usr_name':login_usr})