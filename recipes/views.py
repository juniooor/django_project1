from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'recipes/pages/home.html') 
    # para evitar conflitos de arquivos criar um name space na pasta template

def recipe(request,id):
    return render(request, 'recipes/pages/recipe-view.html') 

    # Nova view para o url seguir