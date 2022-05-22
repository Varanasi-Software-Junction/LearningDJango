from django.db import models
from django.utils.translation import gettext_lazy as _

subjects = (
    (1, "C"),
    (2, "Java"),
    (3, "Python"),
)
class BooksModel(models.Model):

    bookname = models.CharField(max_length=200)
    subject=models.IntegerField(choices=subjects,default=1)

    price = models.IntegerField()
    cover = models.ImageField(upload_to="static/")
    def __str__(self):
        return self.bookname

class SimpleBook(models.Model):

    bookname = models.CharField(max_length=200)
    subject=models.IntegerField(choices=subjects,default=1)

    price = models.IntegerField()
    cover = models.ImageField(upload_to="static/")
    def __str__(self):
        return self.bookname