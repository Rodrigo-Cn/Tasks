from django.contrib.auth.forms import UserCreationForm
from accounts.models import Usuario_Custom
from django import forms

class AccountsForm(UserCreationForm):
    class Meta:
        model = Usuario_Custom
        fields = ['username', 'nome']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'nome' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'password' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
        }
