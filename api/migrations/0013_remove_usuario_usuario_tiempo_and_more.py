# Generated by Django 4.2.4 on 2023-09-03 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_cliente_usuario_tiempo_alter_cliente_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='usuario_tiempo',
        ),
        migrations.AlterField(
            model_name='usuariotiempo',
            name='consentNumber',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='usuariotiempo',
            name='handleColor',
            field=models.CharField(max_length=40),
        ),
    ]
