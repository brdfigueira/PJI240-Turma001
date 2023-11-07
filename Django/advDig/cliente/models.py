from django.db import models
from triagem.models import Usuario, Cliente
from prestador.models import Anexo
from django import forms

class FormCliente(forms.ModelForm):
  class Meta:
    model = Cliente
    fields = ['rg', 'cpf', 'telefone', 'whatsapp', 'endereco', 'profissao']

class FormUp(forms.ModelForm):
  class Meta:
    model = Anexo
    fields = ['anexo']