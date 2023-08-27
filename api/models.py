from django.db import models

# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    second_name = models.CharField(max_length=30, null=False, blank=False)
    first_surname = models.CharField(max_length=30, null=False, blank=False)
    second_surname = models.CharField(max_length=30, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    identification = models.CharField(max_length=60, null=False, blank=False)
    phone = models.CharField(max_length=40, null=False, blank=False)
    cotrol_tiempo = models.ManyToManyField('ControlTiempo', related_name='control_tiempo')

class ControlTiempo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='control_tiempo')
    date = models.DateField(null=False, blank=False)
    minutes_spent = models.IntegerField(null=False, blank=False)
 