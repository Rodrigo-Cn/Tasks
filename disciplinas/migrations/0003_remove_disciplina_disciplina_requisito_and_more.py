# Generated by Django 5.0.4 on 2024-08-06 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplinas', '0002_disciplina_bibliografia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='disciplina_requisito',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='disciplina_requisito',
            field=models.ManyToManyField(blank=True, related_name='disciplinas_relacionadas', to='disciplinas.disciplina'),
        ),
    ]