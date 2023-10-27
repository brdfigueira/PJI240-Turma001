from django.db import models
from triagem.models import Usuario, Cliente
from django import forms

class FormCliente(forms.ModelForm):
  class Meta:
    model = Cliente
    fields = ['rg', 'cpf', 'telefone', 'whatsapp', 'endereco', 'profissao']

