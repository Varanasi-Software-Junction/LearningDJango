<<<<<<< Updated upstream
import datetime
=======
from django.http import HttpResponse
from django.shortcuts import render
from . import book as bookclass


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


def citybyselect(request):
    list = {"up" : "Uttar Pradesh", "mp" : "Madhya Pradesh", "uk" : "Uttarakhand", "hp": "Himanchal Pradesh"  }
    # a = 0
    # b = 0
    result = {}
    option = ""
    # op = "+"
    if request.POST:
        # a = int(request.POST["a"])
        # b = int(request.POST["b"])
        option = request.POST["option"]
        for key, value in list.items():
            if key == option:
                result[key] = value

        # if option == "up":
        #     result = "up"
        # if option == "mp":
        #     result = "mp"
        # if option == "uk":
        #     result = "uk"
        # if option == "hp":
        #     result = "hp"

    return render(request, "citynamebyselect.html", {"result": result, "option": option})


def print(request):
    return render(request, "citynamebyselect.html")

def books(request):
    sub = ""
    book = [bookclass.Book("Basic C", "C", 300),bookclass.Book("Basic C++", "C++", 400),bookclass.Book("Python", "Python", 500)]
    return render(request, "books.html", {"book": book, "sub":sub})




>>>>>>> Stashed changes

from django.shortcuts import render, HttpResponse


# from siteclasses import Book
def sessionremove(request):
    key = ""
    if request.POST:
        key = request.POST["key"]
        try:
            request.session.pop(key)
        except:
            pass

    return render(request, "sessionremove.html", {"key": key})


def sessionset(request):
    key = ""
    value = ""
    if request.POST:
        key = request.POST["key"]
        value = request.POST["value"]
        request.session[key] = value
    return render(request, "sessionset.html", {"key": key, "value": value})


def sessionview(request):
    return render(request, "sessionview.html", {"session": request.session.items()})


def tfquiz(request):
    questions = [{"question": "C is a programming language", "answer": True},
                 {"question": "Java is not a programming language", "answer": False},
                 {"question": "C is not a programming language", "answer": False}]
    qno = 0
    if request.POST:
        qno = int(request.POST["qno"])
        qno += 1
    if qno >= len(questions):
        return HttpResponse("Test Over")
    question = questions[qno]
    return render(request, "tfquiz.html", {"qno": qno, "qnumber": qno + 1, "question": question})


def index(request):
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#reversing-admin-urls
    links = ["admin:index", "aggregates", "all", "between", "initial", "formdata"]
    return render(request, "home.html", {"links": links})


def mysession(request):
    session = request.session
    session[1] = "One"
    return render(request, "session.html", {"session": session})


def test(request):
    return render(request, "bootstrap.html")


def vsj404(request, exception):
    return render(request, "404.html", {"exception": exception}, status=404)


def setCookie(request):
    max_age = 365 * 24 * 60 * 60  # one year
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                                         "%a, %d-%b-%Y %H:%M:%S GMT")

    data = HttpResponse("Cookie Set")
    data.set_cookie("location", 'Varanasi', max_age=max_age, expires=expires)
    return data


def getCookie(request):
    cookie = request.COOKIES.get("location")
    return HttpResponse(cookie)
