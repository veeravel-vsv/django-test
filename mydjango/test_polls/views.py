from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def index(request,users_id):
	return HttpResponse("Hello! Django %s" % users_id)
