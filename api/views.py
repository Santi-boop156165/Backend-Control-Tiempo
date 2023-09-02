from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ClienteSerializer,UsuarioSerializer
from .models import Cliente, ControlTiempo, Usuario, UsuarioTiempo

# Create your views here.

class ControlApiView(APIView):

    def get(self, request, id=0):
        if id > 0:
            try:
                cliente = Cliente.objects.get(id=id)
                serializer = ClienteSerializer(cliente)
                data = {
                    "message": "Success",
                    "cliente": serializer.data
                }
                return Response(data, status=status.HTTP_200_OK)
            except Cliente.DoesNotExist:
                return Response({"message": "Cliente not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            clientes = Cliente.objects.all()
            serializer = ClienteSerializer(clientes, many=True)
            data = {
                "message": "Success",
                "clientes": serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        
        
    
    def post(self, request):
        cliente_data = request.data
        control_tiempo_data = cliente_data.pop('control_tiempo', [])

        cliente_serializer = ClienteSerializer(data=cliente_data)
        if cliente_serializer.is_valid():
            cliente = cliente_serializer.save()

            control_tiempo_instances = []
            for control_data in control_tiempo_data:
                control_data['cliente'] = cliente  # Pasar la instancia de Cliente
                control_tiempo_instances.append(ControlTiempo(**control_data))

            ControlTiempo.objects.bulk_create(control_tiempo_instances)
            
            response_data = {
                "succes": cliente_serializer.data
              
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

 
    def put(self, request, id):
        try:
            cliente = Cliente.objects.get(id=id)
        except Cliente.DoesNotExist:
            return Response({"message": "Cliente not found"}, status=status.HTTP_404_NOT_FOUND)

        cliente_data = request.data
        control_tiempo_data = cliente_data.pop('control_tiempo', [])

        cliente_serializer = ClienteSerializer(instance=cliente, data=cliente_data)
        if cliente_serializer.is_valid():
            cliente = cliente_serializer.save()

            for control_data in control_tiempo_data:
                date = control_data.get('date')
                minutes_spent = control_data.get('minutes_spent')
                id_control = control_data.get('id')
                # Buscar registro existente de ControlTiempo por fecha
                try:
         
                    control_tiempo = ControlTiempo.objects.get(id=id_control,)
                    control_tiempo.minutes_spent = minutes_spent
                    control_tiempo.date = date
                    control_tiempo.save()
                except ControlTiempo.DoesNotExist:
               
                    # Si no existe, crear uno nuevo
                    ControlTiempo.objects.create(cliente=cliente, date=date, minutes_spent=minutes_spent)
            
            response_data = {
                "success": "Cliente and ControlTiempo updated successfully"
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            cliente = Cliente.objects.get(id=id)
            cliente.delete()
            
            return Response({"message": "Cliente deleted"}, status=status.HTTP_200_OK)
        except Cliente.DoesNotExist:
            return Response({"message": "Cliente not found"}, status=status.HTTP_404_NOT_FOUND)
        


class TiempoApiView(APIView):
       
       def get(self, request, id=0):
        if id > 0:
            try:
                cliente = Usuario.objects.get(id=id)
                serializer = UsuarioSerializer(cliente)
                data = {
                    "message": "Success",
                    "cliente": serializer.data
                }
                return Response(data, status=status.HTTP_200_OK)
            except Usuario.DoesNotExist:
                return Response({"message": "Cliente not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            clientes = Usuario.objects.all()
            serializer = UsuarioSerializer(clientes, many=True)
            data = {
                "message": "Success",
                "clientes": serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        
       def post(self, request):
        usuario_data = request.data
        usuario_tiempo_data = usuario_data.pop('control_tiempo', [])  # Use 'usuario_tiempo' instead of 'usuarios'

        usuario_serializer = UsuarioSerializer(data=usuario_data)
        if usuario_serializer.is_valid():
            usuario = usuario_serializer.save()

            usuario_tiempo_instances = []
            for tiempo_data in usuario_tiempo_data:
                tiempo_data['usuario'] = usuario
                usuario_tiempo_instances.append(UsuarioTiempo(**tiempo_data))

            UsuarioTiempo.objects.bulk_create(usuario_tiempo_instances)

            response_data = {
                "success": usuario_serializer.data,  # Correct the key to 'success'
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(usuario_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
       def delete(self, request, id):
        try:
            usuario = Usuario.objects.get(id=id)
            usuario.delete()
            
            return Response({"message": "Usuario deleted"}, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({"message": "Usuario not found"}, status=status.HTTP_404_NOT_FOUND)
       


        