from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path("login/?", views.triagem, name='triagem'),
    path("demanda", views.demandaNovo, name='demanda'),
    path("cliente", views.demandaCliente, name='cliente')
]