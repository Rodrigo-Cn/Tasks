from django.db import models
from pessoas.models import Pessoa
from django.utils import timezone

class Professor(Pessoa):
    titulacao_maxima = models.CharField(max_length=50)
    data_validade = models.DateField(default=timezone.now)

    def is_valid(self):
        return self.data_validade >= timezone.now().date()
    
    def __str__(self):
        return f"Professor: {self.nome}"
