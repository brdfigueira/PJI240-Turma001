from django.urls import path
from . import views

urlpatterns = [
    path('cliente', views.cliente, name='cliente'),
    path('cliente/demandas', views.demandaTodas, name='demandaTodas'),
    path('cliente/demanda/nova', views.demandaNova, name='demandaNova'),
    path('cliente/demanda/<int:demanda_id>', views.demanda, name='demanda'),
    path('cliente/processo/<int:processo_id>', views.processo, name='processo'),
    path('cliente/processos/', views.processos, name='processos'),
    path('cliente/processos/todos', views.processosTodos, name='processosTodos'),
    path('cliente/cadastro', views.cadastro, name='cadastro'),
]
