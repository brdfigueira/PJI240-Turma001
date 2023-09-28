from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# Create your models here.
class Usuario(AbstractUser):
    detalhes = models.TextField(null=True, blank=True)

class Demanda(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    info1 = models.TextField(null=True, blank=True)
    info2 = models.TextField(null=True, blank=True)

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

