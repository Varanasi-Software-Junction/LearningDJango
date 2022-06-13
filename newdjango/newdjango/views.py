from django.shortcuts import render


# from siteclasses import Book


def index(request):
    # https://docs.djangoproject.com/en/dev/ref/contrib/admin/#reversing-admin-urls
    links = ["admin:index", "aggregates", "all", "between", "initial", "formdata"]
    return render(request, "home.html", {"links": links})

def mysession(request):
    session=request.session
    session[1]="One"
    return render(request,"session.html",{"session":session})
def test(request):
    return render(request, "bootstrap.html")
def vsj404(request,exception):
    return render(request, "404.html",{"exception":exception},status=404)
