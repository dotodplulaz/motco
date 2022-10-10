from django.contrib import admin
from django.urls import path,include
from django.conf import settings
# from motcors import views

from django.views.static import serve
#from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
   path('', views.home,name='home'),
    path('dp/', views.index,name='index'),

]
