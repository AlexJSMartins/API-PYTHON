#data_api\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('melhor', views.melhor, name='melhor_filtro'),  # Melhor genérico
    path('ranking', views.ranking, name='ranking_completo'),  # Ranking genérico
    path('melhor-por-categoria', views.melhor_vendedor_por_categoria, name='melhor_por_categoria'),  # Melhor por categoria
    path('analise-por-empregado', views.analise_por_empregado, name='analise_por_empregado'),  # Análise por empregado
    path('analise-por-cidade', views.analise_por_cidade, name='analise_por_cidade'),  # Análise por cidade
    path('analise-por-bandeira', views.analise_por_bandeira, name='analise_por_bandeira'),  # Análise por bandeira
    path('melhor-cidade-ou-bandeira', views.melhor_para_cidade_ou_bandeira, name='melhor_para_cidade_ou_bandeira'),  # Melhor cidade ou bandeira
    path('ranking-cidade-ou-bandeira', views.ranking_para_cidade_ou_bandeira, name='ranking_para_cidade_ou_bandeira'),  # Ranking cidade ou bandeira
]
