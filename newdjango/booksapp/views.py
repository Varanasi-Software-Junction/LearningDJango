from django.db.models import Avg
from django.http import HttpResponse
from django.shortcuts import render

from .forms import TestBookForm, TestBookFormOne
from .models import BooksModel,TestBook


def index(request):
    return HttpResponse("You're at the Books index.")


def allbooks(request):
    # data = BooksModel.objects.all().order_by('bookname')
    data = BooksModel.objects.all().order_by('bookname').reverse()
    # data = BooksModel.objects.all().order_by(Coalesce('bookname','bookname').desc())
    # data = BooksModel.objects.all().order_by(Lower('bookname').desc())
    return render(request, "allbooks.html", {'books': data, "title": "All Books"})


def searchbooks(request):
    data = BooksModel.objects.filter(subject="2")
    return render(request, "allbooks.html", {'books': data, "title": "Search Subject"})


def searchor(request):
    data = BooksModel.objects.filter(subject="2") | BooksModel.objects.filter(subject="1")
    return render(request, "allbooks.html", {'books': data, "title": "Search Subject Or"})


def avg(request):
    data = (BooksModel.objects.filter(subject="2") | BooksModel.objects.filter(subject="1")).aggregate(Avg('price'))
    return render(request, "allbooks.html", {'books': data, "title": "Avg Price"})


def showForm(request):
    return render(request, "testformbook.html", {'testform': TestBookForm(), "title": "Form"})


def showFormInitial(request):
    book = TestBook.objects.get(pk=1)
    print(book.bookname)
    f = TestBookFormOne(initial={"bookname":book.bookname,"subject":book.subject,"price":book.price})
    # print(f)
    # f.save()
    # print(f.is_bound)

    print(f.is_valid())
    if f.is_valid():
        f.save()
    return render(request, "testformbook.html", {'testform': f, "title": "Form with Initial"})


def showForm1(request):
    book = TestBook.objects.get(pk=1)
    f = TestBookFormOne(instance=book)
    # print(f)
    # f.save()
    # print(f.is_bound)

    print(f.is_valid())
    if f.is_valid():
        f.save()
    return render(request, "testformbook.html", {'testform': f, "title": "Form with Instance"})
