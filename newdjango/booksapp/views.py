from django.http import HttpResponse
from .models import BooksModel

def index(request):
    return HttpResponse("You're at the Books index.")