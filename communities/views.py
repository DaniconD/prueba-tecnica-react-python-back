from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request, 'communities/index.html')

def say_hello(request):
  return HttpResponse('Hello World')
