from django.urls import path
from . import views

urlpatterns = [
    path('equipe', views.equipe, name='equipe'),
    path('equipe/processos', views.processos, name='e_processos'),
    path('equipe/processos/<int:user>/<str:status>', views.processos, name='e_processos_user'),
    path('equipe/processos/todos', views.processosTodos, name='e_processosTodos'),
    path('equipe/processo/<int:processo_id>', views.processo, name='e_processo'),
    path('equipe/processo/novo/<int:demanda_id>', views.processoNovo, name='e_processoNovo'),
    path('equipe/processo/<int:proc_id>/atualiza/<int:at_id>', views.atualizacao, name='e_atualiza'),
    path('equipe/demandas/', views.demandas, name='e_demandas'),
    path('equipe/demandas/<int:usuario>/<str:status>', views.demandas, name='e_demandas_user'),
    path('equipe/demandas/<str:status>', views.demandas, name='e_demandas_status'),
    path('equipe/demandas', views.demandas, name='e_demandas'),
    path('equipe/demanda/<int:demanda_id>', views.demanda, name='e_demanda'),
    path('equipe/demanda/<int:demanda_id>/a=<int:acao>/', views.demandaAcolher, name='e_demandaAcolher'),
    path('equipe/clientes/<str:ativos>', views.clientes, name='e_clientes'),
    path('equipe/cliente/<int:cliente_id>', views.cliente, name='e_cliente'),
    path('equipe/<str:tipo>/<int:id>/solicita', views.solicitaNova, name='e_solicitaNova'),
    path('equipe/solicita/<int:solicita_id>', views.solicita, name='e_solicita'),
    path('equipe/solicita/<int:solicita_id>/<str:acao>', views.solicitaProc, name='e_solicitaProc'),
    path('equipe/anexo/<int:anexo_id>/<str:acao>', views.anexo, name='e_anexo'),
    path('equipe/teste/<int:id>', views.teste, name='teste'),
    path('equipe/<str:ref>/<int:id>/solicitas', views.solicitas, name='e_solicitas'),
    path('equipe/<str:ref>/<int:id>/anexos', views.anexos, name='e_anexos'),
    # path('cliente/anexo', views.anexoNovo, name='anexo'),
]
