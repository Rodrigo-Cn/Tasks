from django.db import models
from django.utils import timezone

class Tasks(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=150)
    data = models.DateField(default=timezone.now)
    horario = models.TimeField(default=timezone.make_aware(timezone.datetime(2000, 1, 1, 10, 0, 0)))