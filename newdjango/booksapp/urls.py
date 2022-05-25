from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('allbooks', views.allbooks, name='all'),
path('search', views.searchbooks, name='search'),
path('or', views.searchor, name='searchor'),
]
