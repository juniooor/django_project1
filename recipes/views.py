from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'recipes/home.html') 
    # para evitar conflitos de arquivos criar um name space na pasta template

def contato(request):
    return HttpResponse('contato')

def sobre(request):
    return HttpResponse('sobre')

def testes(request):
    return HttpResponse('Toma esse Response distraido')