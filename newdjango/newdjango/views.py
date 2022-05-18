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

def selecttag(request):
    data=["One","Two","Three"]
    return render(request,"select.html",{"data":data})
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

def addsubradio(request):
    a = 0
    b = 0
    result = 0
    option = ""
    if request.GET:
        a = int(request.GET["a"])
        b = int(request.GET["b"])
        option = request.GET["option"]
        if option == "add":
            result = a+b
        if option == "sub":
            result = a- b
    return render(request, "addsubbyradio.html", {"a": a, "b": b, "result": result})

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

def select(request):
    a = 0
    b = 0
    result = 0
    option = ""
    op = "+"
    if request.POST:
        a = int(request.POST["a"])
        b = int(request.POST["b"])
        option = request.POST["option"]
        if option == "add":
            op = "+"
            result = a+b
        if option == "sub":
            result = a-b
            op = "-"
        if option == "mul":
            result = a*b
            op = "*"
        if option == "div":
            result = a/b
            op = "/"
    return render(request, "selecttag.html", {"a": a, "b": b, "result": result, "op": op})

def check(request):
    a = 0
    b = 0
    result = 0
    option = ""
    op = "+"
    if request.POST:
        a = int(request.POST["a"])
        b = int(request.POST["b"])
        if request.POST["option"]:
            pass
        option = request.POST["option"]
        if option == "checked":
            op = "+"
            result = a+b
        else:
            result = a-b
            op = "-"

    return render(request, "checktag.html", {"a": a, "b": b, "result": result, "op": op})

def loop(request):
    return render(request, "loop.html", {"x": range(2,15), "y": "This is Y"})

def loop1(request):
    d = {"1":"Sachin", "2":"CR"}
    return render(request, "loop1.html", {"x": range(1,11), "d": d})

def printtable(request):
    n = 0
    table = ""
    if request.GET:
        n = int(request.GET["n"])
        table=[ x*n for x in range(1,11)]

    return render(request, "printtable.html", {"n": n, "table": table, "x":range(1,11)})
d={}
def keyvalue(request):
    key = ""
    value = ""
    if request.GET:
        key = str(request.GET["key"])
        value = str(request.GET["value"])
        # d.add(key, value)
        d[key] = value
    return render(request, "keyvalue.html", {"key":key,"d":d,"value":value})

dict={}
def keyvaluedelete(request):
    key = ""
    value = ""
    #d = {}
    opt = ""
    if request.GET:
        key = str(request.GET["key"])
        value = str(request.GET["value"])
        opt = request.GET["option"]
        # d.add(key, value)
        if opt == "add":
            dict[key] = value
        if opt == "delete":
            dict.pop(key)
    return render(request, "keyvaluedelete.html", {"key":key,"dict":dict,"value":value})

result={}
def addshowresult(request):
    key = ""
    value = ""
    #d = {}
    opt = ""
    if request.GET:
        key = str(request.GET["key"])
        value = str(request.GET["value"])
        opt = request.GET["option"]
        # d.add(key, value)
        if opt == "add":
            result[key] = value
        if opt == "delete":
            result.pop(key)
    return render(request, "addresult.html", {"key":key,"result":result,"value":value})

def showresult(request):
    key = ""
    new = {}

    if request.GET:
        key = str(request.GET["key"])


        # d.add(key, value)
        for k in result.keys():
            if key == k:
                new = result[key]
            else:
                pass
    return render(request, "showresult.html", {"new":new,"result":result})




















