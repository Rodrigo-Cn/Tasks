# Generated by Django 5.0.4 on 2024-10-08 14:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='pagamento',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
