# Generated by Django 4.2.4 on 2023-08-22 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_remove_cliente_registros'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='registros',
            field=models.ManyToManyField(related_name='clientes_registrados', to='api.registrocliente'),
        ),
    ]
