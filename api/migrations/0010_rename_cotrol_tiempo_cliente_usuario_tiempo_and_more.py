# Generated by Django 4.2.4 on 2023-09-03 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_cliente_email_cliente_handlecolor_usuario_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='cotrol_tiempo',
            new_name='usuario_tiempo',
        ),
        migrations.AddField(
            model_name='cliente',
            name='consentNumber',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='consentNumber',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
