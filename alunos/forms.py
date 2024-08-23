from .models import Aluno
from django import forms
from pessoas.forms import PessoasForm

class AlunosForm(PessoasForm):
    class Meta:
        model = Aluno
        fields = ['username', 'nome','cpf']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'nome' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'cpf' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'password' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
        }
