# Generated by Django 5.0.4 on 2024-05-14 19:20

import datetime
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='tasks',
            name='horario',
            field=models.TimeField(default=datetime.datetime(2000, 1, 1, 10, 0, tzinfo=datetime.timezone.utc)),
        ),
    ]
