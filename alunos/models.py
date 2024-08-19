from django.db import models
from pessoas.models import Pessoa
from turmas.models import Turma

class Aluno(Pessoa):
    matricula = models.CharField(max_length=20)
    situacao = models.CharField(max_length=100)
    turmas = models.ManyToManyField(Turma)
