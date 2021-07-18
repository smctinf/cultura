from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def cadastro(request):

    if request.method == 'POST':
        form = CadastroForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/cadastrook/')

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

#    form = CadastroForm(widget=forms.RadioSelect, choices=OUTROCURSO)
        form = CadastroForm()

    return render(request, 'cadastro.html', { 'form': form })



def cadastrook(request):
    return render(request, 'cadastrook.html')
