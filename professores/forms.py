from .models import Professor
from django import forms
from pessoas.forms import PessoasForm

class ProfessoresForm(PessoasForm):
    class Meta:
        model = Professor
        fields = ['username', 'nome','cpf']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'nome' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'cpf' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'password' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
        }
