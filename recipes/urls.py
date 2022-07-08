from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('recipes/<int:id>/', views.recipe, name="recipes-receitas"), # Essa recipe chama a view recipe com unico objeto da lista ex: "recipes/1"
    
]
