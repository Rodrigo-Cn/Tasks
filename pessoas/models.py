from django.db import models
from accounts.models import Usuario

class Pessoa(Usuario,models.Model):
    class Meta:
        abstract = True
    cpf = models.CharField(max_length=11)