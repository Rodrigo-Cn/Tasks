from django.forms import ModelForm
from .models import Disciplina, Curso
from django import forms

class DisciplinaForm(ModelForm):
    disciplina_requisito = forms.ModelMultipleChoiceField(
        queryset=Disciplina.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
    
    curso = forms.ModelChoiceField(
        queryset=Curso.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control form-control-user'}),
        label="Curso"
    )
    
    class Meta:
        model = Disciplina
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'carga_horaria': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'ementa': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'bibliografia': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
        }
        labels = {
            'disciplina_requisito': 'Pre-requisitos'
        }
        help_texts = {
            'disciplina_requisito': 'Help Text Aqui'
        }
