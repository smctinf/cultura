from django.contrib import admin
from .models import *

# Register your models here.

class AnoEscolarAdmin(admin.ModelAdmin):
    list_display = ['nome', 'dt_inclusao']
#    list_filter = ['cidade']
    search_fields = ['nome']

admin.site.register(AnoEscolar, AnoEscolarAdmin)

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'dt_inclusao']
#    list_filter = ['cidade']
    search_fields = ['nome']

admin.site.register(Curso, CursoAdmin)

class OutroCursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'dt_inclusao']
#    list_filter = ['cidade']
    search_fields = ['nome']

admin.site.register(OutroCurso, OutroCursoAdmin)

class CandidatoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cpf', 'dt_nascimento', 'curso', 'dt_inclusao']
    list_filter = ['curso']
    search_fields = ['nome']

admin.site.register(Candidato, CandidatoAdmin)

class InstrutorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'dt_inclusao']
    search_fields = ['nome']

admin.site.register(Instrutor, InstrutorAdmin)

class TurmaAdmin(admin.ModelAdmin):
    list_display = ['curso', 'id', 'dt_inclusao']
    search_fields = ['curso__nome']

admin.site.register(Turma, TurmaAdmin)

class Turma_AlunoAdmin(admin.ModelAdmin):
    list_display = ['turma', 'aluno', 'dt_inclusao']
    search_fields = ['aluno__nome']

admin.site.register(Turma_Aluno, Turma_AlunoAdmin)
