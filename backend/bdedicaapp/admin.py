from django.contrib import admin
from .models import MSE, Adolescente, Orientador, AtoInfracional, ContatoAdolescente

# Register your models here.

@admin.register(MSE)
class MSEAdmin(admin.ModelAdmin):
    list_display = ['id', 'processo_num']

@admin.register(Adolescente)
class AdolescenteAdmin(admin.ModelAdmin):
    list_display = ['cpf', 'nome']

@admin.register(Orientador)
class OrientadorAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(AtoInfracional)
class AtoInfracionalAdmin(admin.ModelAdmin):
    list_display = ['nome']

@admin.register(ContatoAdolescente)
class ContatoAdolescenteAdmin(admin.ModelAdmin):
    list_display = ['id_adolescente', 'telefone']