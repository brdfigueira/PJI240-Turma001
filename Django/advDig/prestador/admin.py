from django.contrib import admin
from .models import Cliente, Processo, Anexo, Atualizacao

# Register your models here.
class Cliente(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    list_display_links = ('email')

class Processo(admin.ModelAdmin):
    list_display = ('cliente', 'numero', 'ativo')
    list_filter = ('cliente', 'ativo')
    list_display_links = ('numero')

class Anexo(admin.ModelAdmin):
    list_display = ('cliente', 'descricao')
    list_filter = ('cliente', 'processo')
    list_display_links = ('descricao')

class Atualizacao(admin.ModelAdmin):
    list_display = ('processo', 'data', 'explicado')
    list_filter = ('cliente', 'explicado')
    list_display_links = ('data')