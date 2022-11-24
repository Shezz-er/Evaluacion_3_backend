# Generated by Django 4.1.2 on 2022-11-11 03:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificados',
            fields=[
                ('id_certificado', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('curso', models.CharField(max_length=30)),
                ('version', models.CharField(max_length=15)),
                ('id_validacion', models.CharField(max_length=15, unique=True)),
            ],
        ),
    ]