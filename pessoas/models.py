from django.db import models
from accounts.models import Usuario_Custom

class Pessoa(Usuario_Custom):
    cpf = models.CharField(max_length=11)