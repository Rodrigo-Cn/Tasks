from django.forms import ModelForm
from .models import Disciplina
from django import forms

class DisciplinaForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'carga_horaria': forms.NumberInput(attrs={'class': 'form-control form-control-user'}),
            'ementa': forms.Textarea(attrs={'class': 'form-control form-control-user'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control form-control-user'}),
            'bibliografia': forms.Textarea(attrs={'class': 'form-control form-control-user'}),
            'disciplina_requisito': forms.CheckboxSelectMultiple(),
            'curso': forms.Select(attrs={'class': 'form-control form-control-user'}),
        }
        labels = {
            'disciplina_requisito': 'Pré-requisitos'
        }
        help_texts = {
            'disciplina_requisito': 'Selecione as disciplinas pré-requisito'
        }
