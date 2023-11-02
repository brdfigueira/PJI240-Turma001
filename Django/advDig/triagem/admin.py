from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Demanda, Pendencia, Negativa

# Register your models here.
class UsuarioAdmin(UserAdmin):
    list_display =(
        'username', 'email', 'first_name', 'last_name', 'is_staff'
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('detalhes', 'email')
        })
    )

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Demanda)
admin.site.register(Pendencia)
admin.site.register(Negativa)