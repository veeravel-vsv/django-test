from django.shortcuts import render, get_object_or_404, get_list_or_404, Http404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import LoginUser
from django.urls import reverse
from .form import LoginForm
from django.contrib.auth import logout,login, authenticate
# Create your views here.

def login_page(request):
	return render(request, 'polls/login.html',{'form':LoginForm()})

# def index(request):
# 	try:
# 		user_detail = LoginUser.objects.get(username=request.POST.get('txtUser',False))
# 	except LoginUser.DoesNotExist:
# 		raise Http404("User does not exit")
		
# 	if request.POST['txtPassword'] == user_detail.password:
# 		return render(request, 'polls/index.html',{'usr_name' : user_detail.username})
# 	else:
# 		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def index(request):
	username = request.POST.get('username',False)
	password = request.POST.get('password',False)
	# print(username,password)
	user = authenticate(username = username, password = password)
	print(user,"pass")
	if user is not None:
		if user.is_active:
			login(request,user)
			return render(request,'polls/index.html',{'user_name':username.upper()})
		else:
			return render(request,'polls/login.html',{'form':LoginForm()})
	else:
		return render(request,'polls/login.html',{'form':LoginForm()})

def logout_page(request):
	logout(request)
	return render(request,'polls/login.html',{'form':LoginForm()})