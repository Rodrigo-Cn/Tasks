from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=30)
    carga_horaria = models.IntegerField()
    ementa = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    bibliografia = models.CharField(max_length=100)
    disciplina_requisito = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='disciplinas_relacionadas')    
    def __str__(self):
        return self.nome

