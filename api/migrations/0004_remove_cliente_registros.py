# Generated by Django 4.2.4 on 2023-08-22 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_cliente_registros_alter_registrocliente_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='registros',
        ),
    ]