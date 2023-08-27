from rest_framework import serializers
from .models import Cliente, ControlTiempo



class ControlTiempoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlTiempo
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    control_tiempo = ControlTiempoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Cliente
        fields = ['id','first_name', 'second_name', 'first_surname', 'second_surname', 'age', 'identification', 'phone', 'control_tiempo']