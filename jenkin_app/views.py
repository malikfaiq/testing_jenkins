from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def start_app(request):
    return HttpResponse("hello_jenkins")


def end_app(request):
    return HttpResponse("end_app")
