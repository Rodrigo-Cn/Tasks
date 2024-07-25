from django.db import models
from accounts.models import Usuario

class Pessoa(Usuario,models.Model):
    cpf = models.CharField(max_length=11)