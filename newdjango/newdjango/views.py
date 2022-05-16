from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Welcome abc  to new DJango")


def indrakant(request):
    return HttpResponse("This is Indrakant")


# <<<<<<< Updated upstream
def add(request, a=0, b=0):
    result = "A={0} + B={1} = {2}".format(a, b, a + b)
    return HttpResponse(result)

def fact(request, f):
    factorial = 1
    for i in range(f,1,-1):
        factorial = factorial * i
    return HttpResponse(factorial)

### =======
def abhishek(request):
    return HttpResponse("This is Abhishek")
# >>>>>>> Stashed changes


def html(request):
    return render(request, "hello.html")


# <<<<<<< Updated upstream
def get(request):
    a = 0
    b = 0
    result = 0
    if request.GET:
        a = int(request.GET["a"])
        b = int(request.GET["b"])
        result = a + b
    return render(request, "getform1.html", {"a": a, "b": b, "result": result})


def post(request):
    a = 0
    b = 0
    result = 0
    if request.POST:
        a = int(request.POST["a"])
        b = int(request.POST["b"])
        result = a + b
    return render(request, "postform.html", {"a": a, "b": b, "result": result})
# =======


# def add(request, a=0, b=0):
#     result = "A={0} + {1} = {2}".format(a, b, a + b)
#     return HttpResponse(result)
# def html(request):
#     return render(request,"hello.html")
# >>>>>>> Stashed changes

def addsub(request):
    a = 0
    b = 0
    result = 0
    option=""
    if request.GET:
        a = int(request.GET["a"])
        b = int(request.GET["b"])
        option=request.GET["option"]
        if option=="add":
            result = a + b
        if option=="sub":
            result=a-b
    return render(request, "addsubbybutton.html", {"a": a, "b": b, "result": result})

def addsubpost(request):
    a = 0
    b = 0
    result = 0
    option = ""
    if request.POST:
        a = int(request.POST["a"])
        b = int(request.POST["b"])
        option = request.POST["option"]
        if option == "add":
            result = a+b
        if option == "sub":
            result = a-b
    return render(request, "addsubbypost.html", {"a": a, "b": b, "result": result})
























