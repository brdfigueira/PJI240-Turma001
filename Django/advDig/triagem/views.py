from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Usuario
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def demandaNovo(request):
    return render(request, 'home/index.html')

def demandaCliente(request):
    request.session['demanda'] = True
    return redirect("triagem")

def triagem(request):
    usuario = auth.get_user(request)
    if not usuario.is_authenticated:
        return redirect('home')

    staff = False

    if usuario.is_staff:
        staff = True;
        request.session['staff'] = True

    pk = usuario.pk
    usuario = Usuario.objects.get(pk=pk)
    nome = usuario.first_name
    org = ''
    if staff:
        org = '[Membro da Equipe]'

    messages.add_message(request, messages.SUCCESS, f"Olá, {nome}! {org}")

    if (org == '') and (request.session['demanda'] == True):
        return redirect('home')
    # Trocar home pelo registro de demandas de já clientes

    # if (Perfil and Org == "IPECS"):
    #     return redirect('IPECS')
    # else:
    #     return redirect('Empr')
    return redirect('home')

def login(request):
    usuario = auth.get_user(request)

    if usuario.is_authenticated:
        return redirect('triagem')

    if request.method != 'POST':
        return render(request, 'login/index.html')

    usuario = request.POST.get('Usuario')
    senha = request.POST.get('Senha')

    user = auth.authenticate(request, username=usuario, password=senha)

    if not user:
        messages.add_message(request, messages.ERROR, 'Usuário e/ou senha incorreto')
        return render(request, 'login.html')
    else:
        auth.login(request, user)
        return redirect("triagem")

