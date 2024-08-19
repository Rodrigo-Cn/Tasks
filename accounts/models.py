from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser, models.Model):

    class Meta:
        abstract = True
        
    nome = models.CharField(max_length=100)
