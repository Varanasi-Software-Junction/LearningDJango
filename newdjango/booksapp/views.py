from django.http import HttpResponse
from django.shortcuts import render

from .models import BooksModel


def index(request):
    return HttpResponse("You're at the Books index.")


def allbooks(request):
    data = BooksModel.objects.all()
    return render(request, "allbooks.html", {'books': data,"title":"All Books"})
def searchbooks(request):
    data = BooksModel.objects.filter(subject="2")
    return render(request, "allbooks.html", {'books': data,"title":"Search Subject"})
def searchor(request):
    data = BooksModel.objects.filter(subject="2") | BooksModel.objects.filter(subject="1")
    return render(request, "allbooks.html", {'books': data,"title":"Search Subject Or"})
