import datetime
import json

from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, "bootstrapdemo.html")

