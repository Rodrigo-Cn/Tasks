from django.db import models
from pessoas.models import Pessoa

class Professor(Pessoa):
    titulacao_maxima = models.CharField(max_length=50)