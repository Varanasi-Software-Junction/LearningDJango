
from django.http import HttpResponse
from django.shortcuts import render
from sqlalchemy import create_engine


def index(request):
    return HttpResponse("Welcome to new DJango")

