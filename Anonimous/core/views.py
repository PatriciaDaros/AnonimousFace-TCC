from django.shortcuts import render
from django.http import HttpRespose

def home(request):
    context = {'mensagem':'Sacole'}
    return render(request,'core/index.html', context)