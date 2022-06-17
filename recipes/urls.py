from django.urls import path
from recipes.views import home, contato, sobre, testes



urlpatterns = [
    path('sobre/', sobre), 
    path('contato/', contato), 
    path('', home), 
    path('testes/',  testes)
]
