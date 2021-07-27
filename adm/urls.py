from django.urls import path
from . import views

app_name='adm'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('configuracao/', views.configuracao, name='configuracao'),
    #
    path('relatorios/', views.relatorios, name='relatorios'),
    path('total_por_outros_cursos/', views.totalPorOutrosCursos, name='totalPorOutrosCursos'),
    path('total_candidatos_por_cursos/', views.totalCandidatosPorCursos, name='totalCandidatosPorCursos'),
    path('total_enturmados_por_cursos/', views.totalEnturmadosPorCursos, name='totalEnturmadosPorCursos'),
    path('candidatos_nao_enturmados/', views.candidatosNaoEnturmados, name='candidatosNaoEnturmados'),
    #
    path('cursos/', views.cursos, name='cursos'),
    path('turmas/<int:curso_id>', views.turmas, name='turmas'),
    path('turma_alunos/<int:turma_id>', views.turma_alunos, name='turma_alunos'),
    path('turma_alunos_inclui/<int:turma_id>', views.turma_alunos_inclui, name='turma_alunos_inclui'),
    #
    path('gera_emails/', views.gera_emails, name='gera_emails'),
    path('gera_google/', views.gera_google, name='gera_google'),
    #
    path('change_password', views.change_password, name='change_password'),
    path('sair', views.sair, name='sair'),
]