from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Permissoes)
class PermissoesAdmin(admin.ModelAdmin):
    ...
@admin.register(Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    ...
@admin.register(Laboratorios)
class LaboratoriosAdmin(admin.ModelAdmin):
    ...
@admin.register(Agendamentos)
class AgendamentosAdmin(admin.ModelAdmin):
    ...
@admin.register(Emprestimos)
class EmprestimosAdmin(admin.ModelAdmin):
    ...
@admin.register(EmprestimoExterno)
class EmprestimoExternoAdmin(admin.ModelAdmin):
    ...
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    ...
@admin.register(MaterialEquipamentos)
class MaterialEquipamentosAdmin(admin.ModelAdmin):
    ...
@admin.register(MaterialVidrarias)
class MaterialVidrariasAdmin(admin.ModelAdmin):
    ...
@admin.register(MaterialReagentes)
class MaterialReagentesAdmin(admin.ModelAdmin):
    ...
@admin.register(MaterialConsumiveis)
class MaterialConsumiveisAdmin(admin.ModelAdmin):
    ...
@admin.register(EstoqueLaboratorio)
class EstoqueLaboratorioAdmin(admin.ModelAdmin):
    ...
