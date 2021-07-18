import re
from django import forms
from django.forms import ModelForm, ValidationError
from .models import *

class CadastroForm(ModelForm):

    JACURSOU = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )

    RETORNO_PRESENCIAL = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )


    dt_nascimento = forms.CharField(label='Data Nascimento:', max_length=10, widget = forms.TextInput(attrs={'onkeydown':"mascara(this,data)"}))
    cpf = forms.CharField(label='CPF', max_length=14, widget = forms.TextInput(attrs={'onkeydown':"mascara(this,icpf)"}))
    celular = forms.CharField(required=False, max_length=15, widget = forms.TextInput(attrs={'onkeydown':"mascara(this,icelular)", 'onload' : 'mascara(this,icelular)'}))
    celular_1 = forms.CharField(label= "Celular do Responsável 1", required=False, max_length=15, widget = forms.TextInput(attrs={'onkeydown':"mascara(this,icelular)", 'onload' : 'mascara(this,icelular)'}))
    celular_2 = forms.CharField(label= "Celular do Responsável 2", required=False, max_length=15, widget = forms.TextInput(attrs={'onkeydown':"mascara(this,icelular)", 'onload' : 'mascara(this,icelular)'}))
    ja_cursou = forms.ChoiceField(choices=JACURSOU, widget=forms.RadioSelect, label='O(A) aluno(a) já frequentou algum curso na Oficina Escola ou nos Pontos de Cultura?')
    outro_curso = forms.ModelMultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple({'class': 'no-bullet-list', 'style': 'list-style: none;'}),queryset=OutroCurso.objects.all(), label='Quais outros cursos você gostaria de ver disponíveis na Oficina Escola de Artes e nos Pontos de Cultura?')
    retorno_presencial = forms.ChoiceField(choices=RETORNO_PRESENCIAL, widget=forms.RadioSelect, label='Mediante o retorno das aulas presenciais seguindo todos os protocolos de segurança da vigilância sanitária, o aluno está autorizado a frequentá-las?')

    class Meta:
        model = Candidato
        exclude = ['dt_inclusao']

    def clean_dt_nascimento(self):
        dt = self.cleaned_data["dt_nascimento"]
        dt = dt.split('/')
        dt = dt[2] + '-' + dt[1] + '-' + dt[0]
        return dt

    def clean_cpf(self):
        cpf = validate_CPF(self.cleaned_data["cpf"])
        return cpf
    def clean_celular(self):
        telefone = self.cleaned_data["celular"]
        telefone = telefone.replace("(",'')
        telefone = telefone.replace(")",'')
        telefone = telefone.replace("-",'')
        telefone = telefone.replace(" ",'')
        if telefone != '' and len(telefone) != 11:
            raise ValidationError('Insira um número válido ')
        return telefone
    def clean_celular_1(self):
        telefone = self.cleaned_data["celular_1"]
        telefone = telefone.replace("(",'')
        telefone = telefone.replace(")",'')
        telefone = telefone.replace("-",'')
        telefone = telefone.replace(" ",'')
        if telefone != '' and len(telefone) != 11:
            raise ValidationError('Insira um número válido ')
        return telefone
    def clean_celular_2(self):
        telefone = self.cleaned_data["celular_2"]
        telefone = telefone.replace("(",'')
        telefone = telefone.replace(")",'')
        telefone = telefone.replace("-",'')
        telefone = telefone.replace(" ",'')
        if telefone != '' and len(telefone) != 11:
            raise ValidationError('Insira um número válido ')
        return telefone

