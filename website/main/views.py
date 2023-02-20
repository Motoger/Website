from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>Hello</h4>")

def page(request):
    return HttpResponse('<h4>Homework</h4>')