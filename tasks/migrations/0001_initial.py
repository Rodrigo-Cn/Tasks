# Generated by Django 5.0.4 on 2024-05-07 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=25)),
            ],
        ),
    ]
