from django.contrib.auth.forms import UserCreationForm
from accounts.models import Usuario
from django import forms

class AccountsForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'nome']
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'nome' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'password' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
        }
