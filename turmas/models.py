from django.db import models
from disciplinas.models import Disciplina
from professores.models import Professor
from alunos.models import Aluno

class Turma(models.Model):
    ano = models.IntegerField()
    semestre = models.IntegerField()
    dia_semana = models.IntegerField()
    horarios = models.CharField(max_length=100)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, null=True, blank=True)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, blank=True)
    alunos = models.ManyToManyField(Aluno, blank=True)
