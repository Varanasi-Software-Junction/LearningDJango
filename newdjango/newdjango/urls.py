"""newdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('indrakant/', views.indrakant),
    path('add/<int:a>/<int:b>', views.add),
    path('add/<int:a>/', views.add),
    path('add/', views.add),
    path('html/', views.html),
# <<<<<<< Updated upstream
#     path('get/', views.get),
#     path('post/', views.post),
# =======
    path('abhishek', views.abhishek),
    # path('get', views.get),
    path('fact/<int:f>', views.fact),
    path('get/', views.get ),
    path('post/', views.post),
    path('addsub/', views.addsub),
    path('addsubpost/', views.addsubpost),
    path('addsubradio/', views.addsubradio),
    path('select/', views.select),
    path('check', views.check),
    path('loop', views.loop),
    path('loop1', views.loop1),
    path('printtable', views.printtable),
# >>>>>>> Stashed changes
]











