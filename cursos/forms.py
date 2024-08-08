from django.forms import ModelForm
from django import forms
from .models import Curso

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['nome','descricao']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
        }
