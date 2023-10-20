from django.urls import path
from . import views

urlpatterns = [
    path('equipe', views.equipe, name='equipe'),
    path('equipe/processos', views.processos, name='e_processos'),
    path('equipe/processos/todos', views.processosTodos, name='e_processosTodos'),
    path('equipe/processo/<int:processo_id>', views.processo, name='e_processo'),
    path('equipe/demandas', views.demandas, name='e_demandas'),
    path('equipe/demandas/todas', views.demandasTodas, name='e_demandasTodas'),
    path('equipe/demanda/<int:demanda_id>', views.demanda, name='e_demanda'),
    # path('equipe/clientes/', views.clientes, name='e_clientes'),
    path('equipe/clientes/todos', views.clientesTodos, name='e_clientesTodos'),
    # path('equipe/cliente/<int:cliente_id>', views.cliente, name='e_cliente'),
    # path('cliente/anexo', views.anexoNovo, name='anexo'),
    # path('cliente/processo/05-23', views.proc, name='proc'),
    # path('equipe/processo/05-23', views.procEq, name='proceq'),
    # path('equipe/explicacao/05-23-2', views.explicar, name='explicar'),
    # path('equipe/clientes/todos', views.inicio, name='inicio'),
]
