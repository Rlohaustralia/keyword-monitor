from django.shortcuts import render
from .models import keyword_collection
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello!</h1>")

def add_person(request):
    records = {
        
    }