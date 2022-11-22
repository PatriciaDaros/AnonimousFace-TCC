from django.contrib import admin
from django.urls import path, include, re_path

from meuProjeto.view import home

urlpatterns = [
    path('', home, name='core_home'),
]