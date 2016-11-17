from django.shortcuts import render, get_object_or_404, get_list_or_404, Http404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import LoginUser
from django.urls import reverse
# from .forms import LoginForm
# Create your views here.

def login(request):
	return render(request, 'polls/login.html')

def index(request):
	try:
		user_detail = LoginUser.objects.get(username=request.POST['usrText'])
	except LoginUser.DoesNotExist:
		raise Http404("User does not exit")
		
	if request.POST['pwdText'] == user_detail.password:
		return render(request, 'polls/index.html',{'usr_name' : request.POST['usrText']})
	else:
		return HttpResponseRedirect(request.META.get('HTTP_REFERER'))