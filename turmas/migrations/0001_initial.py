# Generated by Django 5.0.4 on 2024-08-22 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alunos', '0001_initial'),
        ('disciplinas', '0007_alter_disciplina_curso'),
        ('professores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField()),
                ('semestre', models.IntegerField()),
                ('dia_semana', models.IntegerField()),
                ('horarios', models.CharField(max_length=100)),
                ('alunos', models.ManyToManyField(blank=True, to='alunos.aluno')),
                ('disciplina', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='disciplinas.disciplina')),
                ('professor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='professores.professor')),
            ],
        ),
    ]
