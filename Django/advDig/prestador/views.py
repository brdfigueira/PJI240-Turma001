from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import FormAnexo, FormExplicacao, Processo
from triagem.models import Usuario, Cliente, Demanda, FormUsuario, FormDemanda
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q

# Create your views here.

def anexoNovo(request):
    usuario = auth.get_user(request)

    if request.method != 'POST':
        form1 = FormAnexo(prefix="form1")
        contexto = {'form1': form1}
        return render(request, 'prestador/form1.html', contexto)

    return render(request, 'triagem/form1.html')

def proc(request):
    return render(request, 'prestador/proc.html')

def procEq(request):
    return render(request, 'prestador/proceq.html')

def inicio(request):
    return render(request, 'prestador/inicio.html')

def explicar(request):
    usuario = auth.get_user(request)

    if request.method != 'POST':
        form1 = FormExplicacao(prefix="form1")
        contexto = {'form1': form1}
        return render(request, 'prestador/form2.html', contexto)

    return render(request, 'triagem/form1.html')

def teste(request, id):
    objeto = Usuario.objects.get(pk=id)
    print(objeto.email)
    m = objeto.isNovo()
    print(m)
    return HttpResponse(f" é ")

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def processos(request, status="ativos", user="t"):
    lista = Processo.objects.all()
    if status == "ativos":
      lista = lista.filter(Q(ativo=True))
      ativar = 2
    else:
      ativar = 1
    if user != "t":
      lista = lista.filter(Q(cliente__pk=user))
    contexto = {'lista': lista, 'ativar':ativar}

    return render(request, "equipe/processos.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def processosTodos(request):
    lista = Processo.objects.all()
    contexto = {'lista': lista, 'ativar':1}
    return render(request, "equipe/processos.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def processo(request, processo_id):
    processo = get_object_or_404(Processo, id=processo_id)
    contexto = {'processo':processo}
    return render(request, "equipe/processo.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def demandasTodas(request):
    lista = Demanda.objects.all()
    contexto = {'lista': lista, 'ativar':1}
    return render(request, "equipe/demandas.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def demandas(request, usuario='t', status="ativas"):
    lista = Demanda.objects.all()
    ativar=1
    if usuario != 't':
        lista = lista.filter(Q(usuario__pk=usuario))
    if status == "ativas" or not status:
        lista = Demanda.objects.filter(Q(ativa=True))
        ativar=2
    contexto = {'lista': lista, 'ativar':ativar}
    return render(request, "equipe/demandas.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def demanda(request, demanda_id):
    demanda = get_object_or_404(Demanda, id=demanda_id)
    contexto = {'demanda':demanda}
    return render(request, "equipe/demanda.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def clientes(request, ativos):
    lista = Usuario.objects.filter(Q(is_staff=False))
    if ativos == "ativos":
        contexto = {'lista': lista, 'ativar': 2, 'ativos': 1}
    elif ativos == "novos":
        lista = lista.filter(base__isnull=True).filter(Q(demanda__ativa=True),Q(demanda__acolhida=False))
        contexto = {'lista': lista, 'ativar': 3, 'ativos': 1}
    else:
        contexto = {'lista': lista, 'ativar':1, 'ativos': 0}
    return render(request, "equipe/clientes.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def cliente(request, cliente_id):
    usuario = get_object_or_404(Usuario, id=cliente_id)
    contexto = {'usuario':usuario }
    return render(request, "equipe/cliente.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def equipe(request):
    return redirect(processos)