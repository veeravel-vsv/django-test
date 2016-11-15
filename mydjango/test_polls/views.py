from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import LoginUser
# Create your views here.

def index(request,users_id):
	usr_id = get_object_or_404(LoginUser, pk = users_id)
	return render(request, 'polls/index.html',{'a':usr_id})
	# return render(request, 'polls/index.html', {'a':users_id})