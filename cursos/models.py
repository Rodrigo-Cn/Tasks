from django.db import models
import uuid

class Curso(models.Model):
    codigo = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True)
    nome = models.CharField(max_length=60)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome