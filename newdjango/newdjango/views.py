from django.http import HttpResponse
from django.shortcuts import render
from sqlalchemy import create_engine


def index(request):
    return HttpResponse("Welcome abc  to new DJango")


def indrakant(request):
    return HttpResponse("This is Indrakant")


def add(request, a=0, b=0):
    result = "A={0} + {1} = {2}".format(a, b, a + b)
    return HttpResponse(result)
def html(request):
    return render(request,"hello.html")
