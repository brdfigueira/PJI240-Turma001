from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import FormAnexo, FormExplicacao, Processo
from triagem.models import Usuario, Demanda, FormUsuario, FormDemanda
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

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def equipe(request):
    return redirect('processos')

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def processos(request):
    lista = Processo.objects.filter(Q(ativo=True))
    contexto = {'lista': lista, 'ativar':2}

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
def clientesTodos(request):
    lista = Usuario.objects.filter(Q(is_staff=False))
    contexto = {'lista': lista, 'ativar':2}
    return render(request, "equipe/clientes.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def demandasTodas(request):
    lista = Demanda.objects.all()
    contexto = {'lista': lista, 'ativar':1}
    return render(request, "equipe/demandas.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def demanda(request, demanda_id):
    demanda = get_object_or_404(Demanda, id=demanda_id)
    contexto = {'demanda':demanda}
    return render(request, "equipe/demanda.html", contexto)
