from django.db import models

# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    second_name = models.CharField(max_length=30, null=True, blank=True)
    first_surname = models.CharField(max_length=30, null=False, blank=False)
    second_surname = models.CharField(max_length=30, null=True, blank=True)
    age = models.IntegerField(null=False, blank=False)
    identification = models.CharField(max_length=60, null=False, blank=False, unique=True)
    phone = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(null=True, blank=True, max_length=40) 


class ControlTiempo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='control_tiempo')
    date = models.DateField(null=False, blank=False)
    minutes_spent = models.IntegerField(null=False, blank=False)
    consentNumber = models.CharField(null=False, blank=False, max_length=40) 
    handleColor = models.CharField(null=False, blank=False, max_length=40)
    annotations = models.CharField(null=True, blank=True, max_length=255) 
    
 

 
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    second_name = models.CharField(max_length=30, null=True, blank=True)
    first_surname = models.CharField(max_length=30, null=False, blank=False)
    second_surname = models.CharField(max_length=30, null=True, blank=True)
    age = models.IntegerField(null=False, blank=False)
    identification = models.CharField(max_length=60, null=False, blank=False)
    phone = models.CharField(max_length=40, null=False, blank=False)
    email = models.EmailField(null=True, blank=True, max_length=40) 



class UsuarioTiempo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='control_tiempo')
    date = models.DateField(null=False, blank=False)
    minutes_spent = models.IntegerField(null=False, blank=False)
    consentNumber = models.CharField(null=False, blank=False, max_length=40) 
    handleColor = models.CharField(null=False, blank=False, max_length=40)
    annotations = models.CharField(null=True, blank=True, max_length=255) 
 