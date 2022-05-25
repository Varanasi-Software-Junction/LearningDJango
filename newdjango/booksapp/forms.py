from django.forms import ModelForm
from .models import BooksModel,SimpleBook,TestBook
class TestBookForm(ModelForm):
    class Meta:
        model = TestBook
        fields = ['bookname', 'subject', 'price']