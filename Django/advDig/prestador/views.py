from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import FormAnexo, FormExplicacao, Processo, FormNeg, FormProc, FormAtualiz, FormAnexo, Atualizacao, \
    Solicitacao, Anexo
from triagem.models import Usuario, Cliente, Demanda, FormUsuario, FormDemanda, Negativa
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from .funcs import acolherDemanda, atualizarCliente, solicitaNotificar, anexoValidado, anexoRejeitado

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
def processoNovo(request, demanda_id=0):
    if request.method != 'POST':
        if demanda_id == 0:
            form = FormProc()
            dem = 0
        else:
            dem = Demanda.objects.get(pk=demanda_id)
            proc = Processo(demanda=dem)
            form = FormProc(instance=proc)
            dem = dem.pk
        contexto = {'form': form, 'dem': dem}
        return render(request, "equipe/processoform.html", contexto)

    form = FormProc(request.POST)
    proc = form.save(commit=False)
    try:
        proc.cliente = proc.demanda.usuario.base
    except:
        messages.add_message(request, messages.ERROR,
                             f"{proc.demanda.usuario} não é cliente. Tente acolher a demanda.")
        contexto = {'form': form, 'dem': 0}
        return render(request, "equipe/processoform.html", contexto)

    proc.ativo = True
    proc.save()
    chave = proc.pk
    messages.add_message(request, messages.SUCCESS,
                         f"{proc} criado com sucesso")

    return redirect('e_processo', processo_id=chave)

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
        lista = lista.filter(Q(ativa=True))
        ativar = 2
    if status == "novas":
        lista = lista.filter(Q(ativa=True),Q(acolhida=False))
        ativar = 3
    contexto = {'lista': lista, 'ativar':ativar}
    return render(request, "equipe/demandas.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def demanda(request, demanda_id):
    demanda = get_object_or_404(Demanda, id=demanda_id)
    contexto = {'demanda': demanda}
    return render(request, "equipe/demanda.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def demandaAcolher(request, acao, demanda_id):
    demanda = get_object_or_404(Demanda, id=demanda_id)

    if acao == 1:
        if not demanda.acolhida == True:
            if not hasattr(demanda.usuario, 'base'):
              cliente = Cliente(usuario=demanda.usuario)
              cliente.save()
              atualizarCliente(cliente)
              messages.add_message(request, messages.SUCCESS,
                                   f"{cliente} foi salvo como cliente")
            demanda.acolhida = True
            demanda.ativa = True
            demanda.save()
            acolherDemanda(demanda, acao)
            messages.add_message(request, messages.SUCCESS,
                                 f"{demanda} foi acolhida")
        else:
            messages.add_message(request, messages.WARNING,
                                 f"{demanda} já foi acolhida")
    contexto = {'demanda': demanda}

    if acao == 0:
        if demanda.ativa == True:
            if request.method != 'POST':
                form = FormNeg()
                contexto = {'demanda': demanda, 'form': form}
                return render(request, "equipe/rejeitar.html", contexto)
            neg = Negativa(ref=demanda)
            form = FormNeg(request.POST, instance=neg)
            form.save()
            demanda.acolhida = False
            demanda.ativa = False
            demanda.save()
            messages.add_message(request, messages.WARNING,
                                 f"{demanda} foi rejeitada")
            acolherDemanda(demanda, acao)

        else:
            messages.add_message(request, messages.WARNING,
                                 f"A ação não se aplica à {demanda}")
        return render(request, "equipe/demanda.html", contexto)

    return render(request, "equipe/demanda.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def atualizacao(request, proc_id, at_id=0):
    proc = Processo.objects.get(id=proc_id)
    if request.method != 'POST':
        if at_id != 0:
            atualiz = Atualizacao.objects.get(id=at_id)
            form = FormAtualiz(instance=atualiz)
        else:
            atualiz = None
            form = FormAtualiz()
        contexto = {'proc': proc, 'atualiz':atualiz, 'form': form}
        return render(request, 'equipe/atualiz.html', contexto)
    if at_id != 0:
        atualiz = Atualizacao.objects.get(id=at_id)
        form = FormAtualiz(request.POST, instance=atualiz)
    else:
        form = FormAtualiz(request.POST)
    atualiza = form.save(commit=False)
    if not hasattr(atualiza, "processo"):
         atualiza.processo = proc
    if hasattr(atualiza, "explicacao"):
        if atualiza.explicacao == "":
            atualiza.explicado = False
            atualiza.explicacao = None
        else:
            atualiza.explicado = True
    else:
        atualiza.explicado = False
    atualiza.save()
    messages.add_message(request, messages.SUCCESS,
                         f"{proc} atualizado")
    return redirect("e_processo", processo_id=proc_id)

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

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def solicitaNova(request, tipo, id):
    if request.method != 'POST':
        if tipo == 'cliente':
            cliente = Cliente.objects.get(pk=id)
            solicita = Solicitacao(cliente=cliente)
            solicita.save()
        elif tipo == 'processo':
            processo = Processo.objects.get(pk=id)
            cliente = processo.cliente
            solicita = Solicitacao(cliente=cliente)
            solicita.save()
            solicita.processo.add(processo)
        elif tipo == 'demanda':
            demanda = Demanda.objects.get(pk=id)
            if not hasattr(demanda.usuario, 'base'):
                messages.add_message(request, messages.ERROR,
                                     f"Opção inválida: {demanda.usuario} não é cliente")
                return redirect('equipe')
            cliente = demanda.usuario.base
            solicita = Solicitacao(cliente=cliente)
            solicita.save()
            solicita.demanda.add(demanda)
        else:
            messages.add_message(request, messages.ERROR,
                                 f"Opção inválida")
            return redirect('equipe')
        solicita.save()
        chave = solicita.pk
        contexto = {'solicita':solicita}
        return redirect('e_solicita', solicita_id=chave)

    return HttpResponse('!')

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def solicita(request, solicita_id):
    solicita = get_object_or_404(Solicitacao, pk=solicita_id)
    contexto = {'solicita': solicita}
    if request.method != 'POST':
       return render(request, 'equipe/solicita.html', contexto)
    if request.POST['documento'] == '':
       return redirect('e_solicita', solicita_id=solicita_id)
    anexo = Anexo(cliente = solicita.cliente, descricao=request.POST['documento'], solicitacao = solicita)
    anexo.save()
    if solicita.processo.all().exists():
        for processo in solicita.processo.all():
            anexo.processo.add(processo)
    if solicita.demanda.all().exists():
        for demanda in solicita.demanda.all():
            anexo.demanda.add(demanda)
    anexo.save()
    return render(request, 'equipe/solicita.html', contexto)

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def solicitaProc(request, solicita_id, acao):
    solicita = get_object_or_404(Solicitacao, pk=solicita_id)

    if acao == "cancelar":
        chave = solicita.cliente.usuario.pk
        nro = solicita.pk
        solicita.delete()
        messages.add_message(request, messages.SUCCESS,
                             f"A solicitação #{nro} foi cancelada")
        return redirect("e_cliente", cliente_id=chave)
    if acao == "concluir":
        solicita.concluida = True
        solicita.save()
        messages.add_message(request, messages.SUCCESS,
                             f"A solicitação #{solicita.pk} foi concluida")
    if acao == "enviar":
        solicitaNotificar(solicita_id)
        solicita.enviada = True
        solicita.save()
        messages.add_message(request, messages.SUCCESS,
                             f"Um e-mail foi enviado para {solicita.cliente} informando sobre a solicitação #{solicita.pk}")
    return redirect("e_solicita", solicita_id=solicita_id)

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def anexo(request, anexo_id, acao):
    anexo = get_object_or_404(Anexo, pk=anexo_id)
    if acao == "validar":
        anexo.validado = True
        anexo.save()
        if anexo.solicitacao:
            anexoValidado(anexo_id)
            messages.add_message(request, messages.SUCCESS,
                                 f"Anexo #{anexo.pk} validado")
            return redirect("e_solicita", solicita_id=anexo.solicitacao.pk)
    elif acao == "rejeitar":
        anexo.anexo.delete()
        anexo.validado = False
        if anexo.solicitacao:
            anexoRejeitado(anexo_id)
            messages.add_message(request, messages.WARNING,
                                 f"Anexo #{anexo.pk} rejeitado")
            return redirect("e_solicita", solicita_id=anexo.solicitacao.pk)
    elif acao != 'ver':
        messages.add_message(request, messages.ERROR,
                             f"Ação inválida")
    contexto = {'anexo': anexo}
    return render(request, 'equipe/anexo.html', contexto)

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def solicitas(request, ref, id):
    if ref == "cliente":
        referencia = get_object_or_404(Cliente, pk=id)
        lista = referencia.solicitacao_set.all().filter(concluida=False)
    elif ref == "processo":
        referencia = get_object_or_404(Processo, pk=id)
        lista = referencia.solicitacao_set.all().filter(concluida=False)
    elif ref == "demanda":
        referencia = get_object_or_404(Demanda, pk=id)
        lista = referencia.solicitacao_set.all().filter(concluida=False)
    elif ref == "pendentes" and id == 0:
        lista = Solicitacao.objects.all().filter(concluida=False)
    else:
        messages.add_message(request, messages.ERROR,
                             f"Referência inválida para solicitações")
        return redirect('equipe')
    contexto = {'lista': lista, 'tipo': ref}
    return render(request, "equipe/solicitas.html", contexto)

@user_passes_test(lambda user: user.is_authenticated and (user.is_staff))
def anexos(request, ref, id):
    if ref == "cliente":
        referencia = get_object_or_404(Cliente, pk=id)
        lista = referencia.anexo_set.all()
    elif ref == "processo":
        referencia = get_object_or_404(Processo, pk=id)
        lista = referencia.anexo_set.all()
    elif ref == "demanda":
        referencia = get_object_or_404(Demanda, pk=id)
        lista = referencia.anexo_set.all()
    elif ref == "solicita":
        referencia = get_object_or_404(Solicitacao, pk=id)
        lista = referencia.anexo_set.all()
    else:
        messages.add_message(request, messages.ERROR,
                             f"Referência inválida para documentos")
        return redirect('equipe')
    contexto = {'lista': lista, 'tipo': ref}
    return render(request, "equipe/anexos.html", contexto)
