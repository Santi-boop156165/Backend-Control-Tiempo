# Generated by Django 4.2.4 on 2023-09-03 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_cliente_consentnumber_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='usuario_tiempo',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=40, null=True),
        ),
    ]
