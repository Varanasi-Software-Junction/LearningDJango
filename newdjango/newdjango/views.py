from  datetime import datetime
from django.shortcuts import render, HttpResponse
def sessionset(request):
    session=request.session
    session["current"]=str(datetime.now())
    print(session["current"])
    return HttpResponse("Session Set")
def sessionremove(request):
    session=request.session
    session.pop("current")
    return HttpResponse("Session Remove")

def sessionview(request):
    session=request.session
    current=session.get("current")
    if current is None:
        current="None"
    return HttpResponse("Session View " + current)


def index(request):
    return render(request, "bootstrapdemo.html")
