from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('Hello, Welcome to the index page')


def individual_post(request):
    return HttpResponse('Hi, this is where an individual post will be.')
