from django.db import models
from django.contrib.auth.models import User

class Usuario_Custom(User):
        
    nome = models.CharField(max_length=100)
