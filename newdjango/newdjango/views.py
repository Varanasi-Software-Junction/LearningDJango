import datetime

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
