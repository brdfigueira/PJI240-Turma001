from django.db import models
from triagem.models import Usuario, Demanda
from django import forms

# Create your models here.

class Cliente(Usuario):
    Dados = models.TextField(verbose_name="Dados Adicionais")
    class Meta:
        verbose_name = 'Cliente'
class Processo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, verbose_name="Cliente")
    demanda = models.ForeignKey(Demanda, on_delete=models.DO_NOTHING, verbose_name="Queixa Original")
    numero = models.CharField(max_length=255)
    tribunal = models.CharField(max_length=255)
    ativo = models.BooleanField(default=False)

class Anexo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    processo = models.ManyToManyField(Processo)
    descricao = models.TextField(verbose_name="Descrição")
    anexo = models.FileField (blank=True, null=True, upload_to='anexos/%Y/%m')

class Atualizacao(models.Model):
    processo = models.ForeignKey(Processo, on_delete=models.DO_NOTHING)
    detalhes = models.TextField()
    explicacao = models.TextField(verbose_name="Explicação")
    explicado = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Atualização"
        verbose_name_plural = "Atualizações"
