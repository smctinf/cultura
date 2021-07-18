from django import forms
from django.forms import ModelForm, ValidationError
from aulas.models import *

"""
class TurmaAlunosIncluiForm(ModelForm):

    class Meta:
        model = Turma_Aluno
        exclude = ['turma', 'dt_inclusao']
"""

class TurmaAlunosIncluiForm(forms.Form):
    def __init__(self, turma, *args,**kwargs):
        super (TurmaAlunosIncluiForm,self).__init__(*args, **kwargs)

        selecionados = Turma_Aluno.objects.filter(turma=turma)
        lista=[]
        for selecionado in selecionados:
            lista.append(selecionado.aluno.pk)
        self.fields['aluno'] = forms.ModelChoiceField(queryset=Candidato.objects.exclude(pk__in=lista))

