from django.forms import ModelForm
from .models import Disciplina
from django import forms

class DisciplinaForm(ModelForm):

    class Meta:
        model = Disciplina
        fields = ['nome','carga_horaria','ementa','descricao','bibliografia']
        widgets = {
            'nome' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'carga_horaria' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'ementa' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'descricao' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'bibliografia' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
        }