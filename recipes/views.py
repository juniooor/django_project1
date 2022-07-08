from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

from utils.recipes.factory import make_recipe
# Create your views here.

def home(request):
    return render(request, 'recipes/pages/home.html', context= { 'recipes': [make_recipe() for _ in range(10)]}) 
    # para evitar conflitos de arquivos criar um name space na pasta template

def recipe(request,id):
    return render(request, 'recipes/pages/recipe-view.html',
     context= {'recipe':make_recipe(),
    'is_detail_page': True,
    }) 

    # Nova view para o url seguir