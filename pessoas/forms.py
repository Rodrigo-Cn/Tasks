from .models import Pessoa
from django import forms
from accounts.forms import AccountsForm

class PessoasForm(AccountsForm):
    class Meta:
        model = Pessoa
        fields = ['username', 'nome','cpf']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'nome' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'cpf' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'password' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
        }
