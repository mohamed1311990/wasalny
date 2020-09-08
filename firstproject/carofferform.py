from django.shortcuts import render
from django.http import HttpResponse


def caroffer(request):
    return render(request, "carofferform.html")
