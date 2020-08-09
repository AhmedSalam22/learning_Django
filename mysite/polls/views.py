from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse("<P><strong>This site still under devlopment</strong></p>")

def index(request):
    return HttpResponse("Hello, world. 7ec3b3cf is the polls index.")
