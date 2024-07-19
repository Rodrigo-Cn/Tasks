from django.forms import ModelForm
from .models import Tasks
from django import forms

class TasksForm(ModelForm):

    class Meta:
        model = Tasks
        fields = '__all__'
        widgets = {
            'titulo' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'descricao' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'status' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'data' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
            'horario' : forms.TextInput(attrs={'class':'form-control form-control-user'}),
        }