# Generated by Django 5.0.4 on 2024-08-08 12:08

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=60)),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
    ]