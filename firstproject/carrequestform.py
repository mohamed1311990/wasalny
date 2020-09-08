from django.shortcuts import render
from django.http import HttpResponse


def carrequest(request):
    return render(request, "carrequestform.html")
