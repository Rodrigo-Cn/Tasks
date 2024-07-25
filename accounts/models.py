from django.db import models
from django.contrib.auth.models import User

class Usuario(User, models.Model):
    nome = models.CharField(max_length=100)
