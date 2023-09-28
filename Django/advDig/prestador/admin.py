from django.contrib import admin
from .models import Cliente, Processo, Anexo, Atualizacao

# Register your models here.
class ClienteAdm(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    list_display_links = ['email']

class ProcessoAdm(admin.ModelAdmin):
    list_display = ('cliente', 'numero', 'ativo')
    list_filter = ('cliente', 'ativo')
    list_display_links = ['numero']

class AnexoAdm(admin.ModelAdmin):
    list_display = ('cliente', 'descricao')
    list_filter = ['cliente']
    list_display_links = ['descricao']

class AtualizacaoAdm(admin.ModelAdmin):
    list_display = ('processo', 'data', 'explicado')
    list_filter = ('processo', 'explicado')
    list_display_links = ['data']

admin.site.register(Cliente, ClienteAdm)
admin.site.register(Processo, ProcessoAdm)
admin.site.register(Anexo, AnexoAdm)
admin.site.register(Atualizacao, AtualizacaoAdm)