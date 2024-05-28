# Generated by Django 5.0.4 on 2024-04-11 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=50, verbose_name='Nombre')),
                ('shor_name', models.CharField(default=' ', max_length=20, verbose_name='Nombre Corto')),
                ('amulate', models.BooleanField(default=False, verbose_name='Anulado')),
            ],
        ),
    ]
