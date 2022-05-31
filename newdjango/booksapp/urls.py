from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allbooks', views.allbooks, name='all'),
path('lt', views.between, name='between'),
    path('search', views.searchbooks, name='search'),
    path('or', views.searchor, name='searchor'),
    path('avg', views.avg, name='avg'),
    path('form', views.showForm, name='form'),
path('formone', views.showForm1, name='form1'),
path('initial', views.showFormInitial, name='initial'),
]
