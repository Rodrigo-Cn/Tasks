# Generated by Django 5.0.4 on 2024-10-08 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplinas', '0007_alter_disciplina_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='disciplina_requisito',
            field=models.ManyToManyField(blank=True, related_name='disciplinas_relacionadas', to='disciplinas.disciplina'),
        ),
    ]
