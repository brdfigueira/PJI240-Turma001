from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from triagem.models import Usuario, Demanda, FormUsuario, FormDemanda
from prestador.models import Processo, Cliente, Anexo, Solicitacao
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.db.models import Q
from .models import FormCliente, FormUp

# Create your views here.

@user_passes_test(lambda user: user.is_authenticated and (not user.is_staff))
def cliente(request):
    pendencias(request)
    usuario = auth.get_user(request)
    usuario = Usuario.objects.get(pk=usuario.pk)
    chave = usuario.pk

    lista = Demanda.objects.filter(Q(usuario=chave), Q(ativa=True))
    contexto = {'usuario':chave, 'lista': lista}

    return render(request, "cliente/inicio.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (not user.is_staff))
def demandaTodas(request):
    usuario = auth.get_user(request)
    usuario = Usuario.objects.get(pk=usuario.pk)
    chave = usuario.pk

    lista = Demanda.objects.filter(usuario=chave)
    contexto = {'usuario':chave, 'lista': lista}

    return render(request, "cliente/demTodas.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (not user.is_staff))
def demanda(request, demanda_id):
    demanda = get_object_or_404(Demanda, id=demanda_id)

    usuario = auth.get_user(request)
    usuario = Usuario.objects.get(pk=usuario.pk)
    chave = usuario.pk

    if not chave == demanda.usuario.pk:
        messages.add_message(request, messages.ERROR, "Entrada não disponível")
        return redirect('triagem')

    contexto = {'demanda':demanda}

    return render(request, "cliente/demanda.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (not user.is_staff))
def processo(request, processo_id):
    processo = get_object_or_404(Processo, id=processo_id)

    usuario = auth.get_user(request)
    usuario = Usuario.objects.get(pk=usuario.pk)
    chave = usuario.pk

    if not chave == processo.cliente.usuario.pk:
        messages.add_message(request, messages.ERROR, "Entrada não disponível")
        return redirect('triagem')

    contexto = {'processo':processo}

    return render(request, "cliente/processo.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (not user.is_staff))
def processos(request):
    user = auth.get_user(request)
    user = Usuario.objects.get(pk=user.pk)
    client = Cliente.objects.get(usuario = user)

    lista = Processo.objects.filter(Q(cliente = client), Q(ativo=True))
    contexto = {'lista': lista, 'ativar':2}

    return render(request, "cliente/processos.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (not user.is_staff))
def processosTodos(request):
    user = auth.get_user(request)
    user = Usuario.objects.get(pk=user.pk)
    client = Cliente.objects.get(usuario = user)

    lista = Processo.objects.filter(Q(cliente = client))
    contexto = {'lista': lista, 'ativar':1}

    return render(request, "cliente/processos.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (not user.is_staff))
def cadastro(request):
    pk = auth.get_user(request).pk
    usuario = Usuario.objects.get(pk=pk)
    instance = Cliente.objects.get(usuario__pk=pk)

    if request.method != 'POST':
        form = FormCliente(instance=instance)
        contexto = {'usuario': usuario, 'form': form}

        return render(request, 'cliente/form.html', contexto)

    cliente = FormCliente(request.POST, instance=instance)
    cliente.save()

    pendencias(request)

    messages.add_message(request, messages.SUCCESS, "Atualizado")

    return redirect('cliente')

@user_passes_test(lambda user: user.is_authenticated and (not user.is_staff))
def demandaNova(request):
    pk = auth.get_user(request).pk
    usuario = Usuario.objects.get(pk=pk)

    if request.method != 'POST':
        form = FormDemanda()
        contexto = {'form': form}
        return render(request, 'cliente/demandaForm.html', contexto)

    instancia = Demanda(usuario=usuario)
    form = FormDemanda(request.POST, instance=instancia)
    demanda = form.save()

    messages.add_message(request, messages.SUCCESS, "Sua nova demanda foi encaminhada para a profissional. Aguarde retorno.")

    return redirect('cliente')

def pendencias(request):
    user = auth.get_user(request)
    user = Usuario.objects.get(pk=user.pk)
    if hasattr(user, 'base'):
        if not user.base.cpf:
            request.session['pendencia'] = 1
        else:
            request.session['pendencia'] = 0
        teste = user.base.solicitacao_set.filter(Q(concluida=False), Q(enviada=True)).filter(anexo__validado=False).distinct().count()
        print(user.base.solicitacao_set.filter(Q(concluida=False), Q(enviada=True)).filter(anexo__validado=False).distinct())
        if teste > 0:
            request.session['solicita'] = teste
        else:
            request.session['solicita'] = 0

@user_passes_test(lambda user: user.is_authenticated and (not user.is_staff))
def solicitacoes(request):
    user = auth.get_user(request)
    user = Usuario.objects.get(pk=user.pk)
    client = Cliente.objects.get(usuario = user)

    lista = Solicitacao.objects.filter(Q(cliente = client),Q(concluida=False), Q(enviada=True), Q(anexo__validado=False)).distinct()
    contexto = {'lista': lista, 'ativar':2}

    return render(request, "cliente/solicitas.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (not user.is_staff))
def solicitacao(request, id):
    user = auth.get_user(request)
    user = Usuario.objects.get(pk=user.pk)
    client = Cliente.objects.get(usuario = user)

    solicita = get_object_or_404(Solicitacao, pk=id, cliente=client)
    form = FormUp()
    contexto = {'solicita': solicita, 'form':form, 'ativar':2}

    return render(request, "cliente/solicita.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (not user.is_staff))
def anexos(request):
    user = auth.get_user(request)
    user = Usuario.objects.get(pk=user.pk)
    client = Cliente.objects.get(usuario = user)

    lista = Anexo.objects.filter(Q(cliente = client)).distinct()
    contexto = {'lista': lista, 'ativar':2}

    return render(request, "cliente/anexos.html", contexto)


@user_passes_test(lambda user: user.is_authenticated and (not user.is_staff))
def anexo(request, id, acao):
    user = auth.get_user(request)
    user = Usuario.objects.get(pk=user.pk)
    client = Cliente.objects.get(usuario=user)
    if request.method != 'POST' and acao == 'ver':
        anexo = get_object_or_404(Anexo, pk=id, cliente=client)
        form = FormUp()
        contexto = {'anexo': anexo, 'form': form, 'ativar': 2}

        return render(request, "cliente/anexo.html", contexto)
    if acao == 'anexar':
        instancia = get_object_or_404(Anexo, pk=id, cliente=client)
        form = FormUp(request.POST, request.FILES, instance=instancia)
        anexo = form.save()
        pendencias(request)
        if hasattr(anexo, 'solicitacao'):
            if anexo.solicitacao != '':
                return redirect(solicitacao, id=anexo.solicitacao.pk)
        return redirect('anexo', id=id, acao="ver")
