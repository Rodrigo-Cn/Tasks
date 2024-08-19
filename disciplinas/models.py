from django.db import models
from cursos.models import Curso

class Disciplina(models.Model):
    nome = models.CharField(max_length=30)
    carga_horaria = models.IntegerField()
    ementa = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    bibliografia = models.CharField(max_length=100)
    disciplina_requisito = models.ManyToManyField(
        'self',
        blank=True,
        related_name='disciplinas_relacionadas',
        symmetrical=False,
        null=True
    )

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome

