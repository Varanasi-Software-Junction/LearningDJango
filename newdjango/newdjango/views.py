from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Welcome abc  to new DJango")


def indrakant(request):
    return HttpResponse("This is Indrakant")


def add(request, a=0, b=0):
    result = "A={0} + {1} = {2}".format(a, b, a + b)
    return HttpResponse(result)


def html(request):
    return render(request, "hello.html")


def get(request):
    a = 0
    b = 0
    result = 0
    if request.GET:
        a = int(request.GET["a"])
        b = int(request.GET["b"])
        result = a + b
    return render(request, "getform.html", {"a": a, "b": b, "result": result})


def post(request):
    a = 0
    b = 0
    result = 0
    if request.POST:
        a = int(request.POST["a"])
        b = int(request.POST["b"])
        result = a + b
    return render(request, "postform.html", {"a": a, "b": b, "result": result})
