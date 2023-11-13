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
    path('cliente/solicitas', views.solicitacoes, name='solicitas'),
    path('cliente/solicita/<int:id>', views.solicitacao, name='solicita'),
    path('cliente/anexos', views.anexos, name='anexos'),
    path('cliente/anexo/<int:id>/<str:acao>', views.anexo, name='anexo'),
]
