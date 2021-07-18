from aulas.models import *
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import *


from django.db.models import Count


# Create your views here.

@login_required
def inicio(request):
    return render(request, 'inicio.html')


@login_required
def configuracao(request):
    return render(request, 'configuracao.html')


@login_required
def relatorios(request):
    return render(request, 'relatorios.html')


@login_required
def cursos(request):

    cursos = Curso.objects.all()

    return render(request, 'cursos.html', { 'cursos': cursos })


@login_required
def turmas(request, curso_id):

    turmas = Turma.objects.filter(curso_id=curso_id)

    return render(request, 'turmas.html', { 'turmas': turmas })


@login_required
def turma_alunos(request, turma_id):

    turma = Turma.objects.get(id=turma_id)

    alunos = Turma_Aluno.objects.filter(turma_id=turma_id)

    return render(request, 'turma_alunos.html', { 'turma': turma, 'alunos': alunos })


@login_required
def turma_alunos_inclui(request, turma_id):

    turma = Turma.objects.get(id=turma_id)

    if request.method == 'POST':
        form = TurmaAlunosIncluiForm(turma, request.POST)

        if form.is_valid():
            aux = Turma_Aluno(turma=turma, aluno=form.cleaned_data['aluno'])
            aux.save()
            form = TurmaAlunosIncluiForm(turma)
        else:
            # Se teve erro:
            print('Erro: ', form.errors)
            erro_tmp = str(form.errors)
            erro_tmp = erro_tmp.replace('<ul class="errorlist">', '')
            erro_tmp = erro_tmp.replace('</li>', '')
            erro_tmp = erro_tmp.replace('<ul>', '')
            erro_tmp = erro_tmp.replace('</ul>', '')
            erro_tmp = erro_tmp.split('<li>')
            erro_tmp[2] = erro_tmp[2].replace('&amp;quot;', '')

            messages.error(request, erro_tmp[1] + ': ' + erro_tmp[2])
    else:

        form = TurmaAlunosIncluiForm(turma)

    alunos = Turma_Aluno.objects.filter(turma_id=turma_id)

    return render(request, 'turma_alunos_inclui.html', { 'form': form, 'alunos':alunos, 'turma': turma })


@login_required
def totalPorOutrosCursos(request):

    outros_cursos = OutroCurso.objects.all()

    total_candidatos = Candidato.objects.count()

    totais = []

    for outro_curso in outros_cursos:

        candidatos = Candidato.objects.filter(outro_curso=outro_curso).count()

        totais.append({'outro_curso': outro_curso, 'total': candidatos})

    return render(request, 'total_por_outros_cursos.html', { 'totais': totais, 'total_candidatos': total_candidatos })


@login_required
def totalCandidatosPorCursos(request):

    cursos = Curso.objects.all()

    total_candidatos = Candidato.objects.count()

    totais = []

    for curso in cursos:

        candidatos = Candidato.objects.filter(curso=curso).count()

        totais.append({'curso': curso, 'total': candidatos})

    return render(request, 'total_candidatos_por_cursos.html', { 'totais': totais, 'total_candidatos': total_candidatos })


@login_required
def totalEnturmadosPorCursos(request):

    cursos = Curso.objects.all()

    total_enturmacao = Turma_Aluno.objects.count()

    totais = []

    for curso in cursos:
        turmas = Turma.objects.filter(curso=curso)

        total = 0
        for turma in turmas:
            total += Turma_Aluno.objects.filter(turma=turma).count()

        totais.append({'curso': curso, 'total': total})

    return render(request, 'total_enturmados_por_cursos.html', { 'totais': totais, 'total_enturmacao': total_enturmacao })



@login_required
def candidatosNaoEnturmados(request):

    candidatos = Candidato.objects.all()

    candidatos_nao_enturmados = []

    total = 0

    for candidato in candidatos:
        encontrou = Turma_Aluno.objects.filter(aluno=candidato)

        if encontrou.count() == 0:
            total += 1
            candidatos_nao_enturmados.append({'candidato': candidato})

    return render(request, 'candidatos_nao_enturmados.html', { 'total': total, 'candidatos_nao_enturmados': candidatos_nao_enturmados })


# ===========================================

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Senha alterada.')
            return redirect('change_password')
        else:
            messages.error(request, 'Corrigir o erro apresentado.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', { 'form': form })


@login_required
def sair(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/accounts/logout')
    else:
        return redirect('/accounts/login')
