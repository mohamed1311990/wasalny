from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def registeration(request):
    return render(request, "registeration.html")

def login(request):
    return render(request, "Login.html")
