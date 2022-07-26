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
from django.urls import path, include

from . import views
from django.urls import path, include
urlpatterns = [

    path('admin/', admin.site.urls),

    path('', views.index),
<<<<<<< Updated upstream
    path('vsjpolls/', include('vsjpolls.urls')),
    path('books/', include('booksapp.urls')),
    path('test', views.test),
    path('session', views.mysession),
path('setcookie', views.setCookie),
path('getcookie', views.getCookie),

=======
    path('indrakant/', views.indrakant),
    path('add/<int:a>/<int:b>', views.add),
    path('add/<int:a>/', views.add),
    path('add/', views.add),
    path('html/', views.html),
    path('get/', views.get),
    path('post/', views.post),
# <<<<<<< HEAD
    path('addsub/', views.addsub),
    path('addsubpost/', views.addsubpost),
    path('addsubradio/', views.addsubradio),
    path('select/', views.select),
    path('check', views.check),
    path('loop', views.loop),
    path('loop1', views.loop1),
    path('printtable', views.printtable),
    path('keyvalue/', views.keyvalue),
    path('keyvaluedelete/', views.keyvaluedelete),
    path('addshowresult/', views.addshowresult),
    path('showresult/', views.showresult),
    path('citybyselect/', views.citybyselect),
    path('print/', views.print),
    path('books/', views.books),
# >>>>>>> Stashed changes
# =======
#     path('vsjpolls/', include('vsjpolls.urls')),
     path('myapp/', include('myownapp.urls')),
# >>>>>>> cf7bde04e9f53d98d047ae4c502bf5fe4e319596
>>>>>>> Stashed changes
]
handler404 = views.vsj404
