from django.db import models
from triagem.models import Usuario, Demanda
from django import forms

# Create your models here.

class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, related_name="base", verbose_name="Usuário", on_delete=models.CASCADE)
    dados = models.TextField(verbose_name="Dados Adicionais")
    class Meta:
        verbose_name = 'Cliente'
    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"

class Processo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, verbose_name="Cliente")
    demanda = models.ForeignKey(Demanda, on_delete=models.DO_NOTHING, verbose_name="Queixa Original")
    numero = models.CharField(max_length=255)
    tribunal = models.CharField(max_length=255)
    ativo = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.numero} {self.tribunal}"

class Anexo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    processo = models.ManyToManyField(Processo)
    demanda = models.ManyToManyField(Demanda)
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

class FormAnexo(forms.ModelForm):
    class Meta:
        model = Anexo
        fields = ['demanda', 'descricao', 'anexo']

class FormExplicacao(forms.ModelForm):
    class Meta:
        model = Atualizacao
        fields = ['explicacao']

class Docs(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    processo = models.ManyToManyField(Processo)
    demanda = models.ManyToManyField(Demanda)
    anexos = models.ManyToManyField(Anexo)
    class Meta:
        verbose_name = "Documentos"
        verbose_name_plural = "Documentos"