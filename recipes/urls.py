from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe), # Essa recipe chama a view recipe com unico objeto da lista ex: "recipes/1"
    
]
