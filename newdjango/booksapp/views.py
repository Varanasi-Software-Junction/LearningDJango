from django.http import HttpResponse
from .models import BooksModel
from .models import SimpleBook

def index(request):
    return HttpResponse("You're at the Books index.")