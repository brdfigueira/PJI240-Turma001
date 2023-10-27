from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from django.db.models import Q
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# Create your models here.
class Usuario(AbstractUser):
    detalhes = models.TextField(null=True, blank=True)
    def isNovo(self):
        try:
            m = self.base
            m = False
        except:
            m = True
        n = self.demanda_set.filter(Q(ativa=True),Q(acolhida=False)).exists()
        return m and n

    def isAtivo(self):
        try:
            m = self.base.processo_set.filter(ativo=True).exists()
        except:
            m = False
        return m or self.demanda_set.filter(ativa=True).exists()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, related_name="base", verbose_name="Usuário", on_delete=models.CASCADE)
    rg = models.IntegerField(verbose_name="RG", blank=True, null=True)
    cpf = models.IntegerField(verbose_name="CPF", blank=True, null=True)
    telefone = models.IntegerField(blank=True, null=True)
    whatsapp = models.BooleanField(default=False)
    endereco = models.TextField(verbose_name="Endereço", blank=True, null=True)
    profissao = models.TextField(verbose_name="Profissão", blank=True, null=True)
    class Meta:
        verbose_name = 'Cliente'
    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}"

class Pendencia(models.Model):
    usuario = models.ForeignKey(Usuario, verbose_name="Usuário", on_delete=models.CASCADE)
    descricao = models.TextField(verbose_name="Descrição")
    url = models.URLField()
    tipo = models.CharField(max_length=50)
    chave = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Pendência'
    def __str__(self):
        return f"{self.usuario.first_name} {self.usuario.last_name}-#{self.pk}"

class Demanda(models.Model):
    data = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    info1 = models.TextField(null=True, blank=True)
    info2 = models.TextField(null=True, blank=True)
    ativa = models.BooleanField(default=True)
    acolhida = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.usuario}-{self.pk}"

class Negativa(models.Model):
    ref = models.OneToOneField(Demanda, on_delete=models.CASCADE)
    texto = models.TextField(verbose_name="Justificativa para rejeição")
    def __str__(self):
        return f"{self.ref}"

class FormUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'detalhes', 'email', 'password']
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_id = 'id-exampleForm'
    #     self.helper.form_class = 'blueForms'
    #     self.helper.form_method = 'post'
    #     self.helper.form_action = 'submit_survey'
    #     self.helper.add_input(Submit('submit', 'Submit'))

class FormDemanda(forms.ModelForm):
    class Meta:
        model = Demanda
        fields = ['info1', 'info2']

