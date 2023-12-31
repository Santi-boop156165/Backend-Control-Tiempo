# Generated by Django 4.2.4 on 2023-08-27 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_cliente_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('first_surname', models.CharField(max_length=30)),
                ('second_surname', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('identification', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioTiempo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('minutes_spent', models.IntegerField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tiempos', to='api.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='usuario_tiempo',
            field=models.ManyToManyField(related_name='usuarios', to='api.usuariotiempo'),
        ),
    ]
