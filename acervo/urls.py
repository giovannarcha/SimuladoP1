from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_livros, name='lista'),
    path('novo/', views.novo_livro, name='novo_livro'),
    path('buscar/', views.buscar_livros, name='buscar'),
]