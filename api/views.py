from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework.views import APIView
from .serializers import ClienteSerializer,UsuarioSerializer,ControlTiempoSerializer,UsuarioTiempoSerializer
from .models import Cliente, ControlTiempo, Usuario, UsuarioTiempo
from django.db import transaction
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
            page_number = request.query_params.get('page', 1)
            clientes = Cliente.objects.all()
            paginator = Paginator(clientes, 6)
            current_page = paginator.get_page(page_number)
            serializer = ClienteSerializer(current_page, many=True)
            data = {
                "message": "Success",
                "clientes": serializer.data,
                "page_number": current_page.number,
                "total_pages": paginator.num_pages
            }
            return Response(data, status=status.HTTP_200_OK)
        
        
    
    def post(self, request):
        with transaction.atomic(): 
            cliente_data = request.data
            control_tiempo_data = cliente_data.pop('control_tiempo', [])
            
            cliente_serializer = ClienteSerializer(data=cliente_data)
            if not cliente_serializer.is_valid():
                return Response(cliente_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
            cliente = cliente_serializer.save()
            
            for item in control_tiempo_data:
                item['cliente'] = cliente.id
            
            control_tiempo_serializer = ControlTiempoSerializer(data=control_tiempo_data, many=True)
            
            if not control_tiempo_serializer.is_valid():
                return Response(control_tiempo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            control_tiempo_serializer.save()
            
            return Response({"success": cliente_serializer.data}, status=status.HTTP_201_CREATED)
      

 
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
                consentNumber = control_data.get('consentNumber')
                handleColor = control_data.get('handleColor')
                id_control = control_data.get('id')
                # Buscar registro existente de ControlTiempo por fecha
                try:
         
                    control_tiempo = ControlTiempo.objects.get(id=id_control,)
                    control_tiempo.minutes_spent = minutes_spent
                    control_tiempo.date = date
                    control_tiempo.consentNumber = consentNumber
                    control_tiempo.handleColor = handleColor
                    control_tiempo.save()
                except ControlTiempo.DoesNotExist:
               
                    # Si no existe, crear uno nuevo
                    ControlTiempo.objects.create(cliente=cliente, date=date, minutes_spent=minutes_spent, consentNumber=consentNumber, handleColor=handleColor)
            
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
            sorted_data = sorted(serializer.data, key=lambda x: min([control['minutes_spent'] for control in x['control_tiempo']]) if x['control_tiempo'] else float('inf'))
            data = {
                "message": "Success",
                "clientes": sorted_data
            }
            return Response(data, status=status.HTTP_200_OK)
        
       def post(self, request):
        usuario_data = request.data
        usuario_tiempo_data = usuario_data.pop('control_tiempo', []) 


        usuario_serializer = UsuarioSerializer(data=usuario_data)
        if usuario_serializer.is_valid():
            usuario = usuario_serializer.save()

            usuario_tiempo_instances = []
            for tiempo_data in usuario_tiempo_data:
                tiempo_data['usuario'] = usuario
                usuario_tiempo_instances.append(UsuarioTiempo(**tiempo_data))

            UsuarioTiempo.objects.bulk_create(usuario_tiempo_instances)

            response_data = {
                "success": usuario_serializer.data,  
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
       


class ControlTiempoCreateView(APIView):

    def get(self, request, cliente_id):
        try:
            control_tiempos = ControlTiempo.objects.filter(cliente=cliente_id)
            control_tiempo_serializer = ControlTiempoSerializer(control_tiempos, many=True)
            
            if control_tiempos:
                return Response({"message": "Success", "control_tiempo": control_tiempo_serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "No se encontraron registros para el cliente con ID {}".format(cliente_id)}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": "Error interno del servidor", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        control_tiempo_data = request.data

        control_tiempo_serializer = ControlTiempoSerializer(data=control_tiempo_data)
        if not control_tiempo_serializer.is_valid():
            return Response(control_tiempo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        control_tiempo = control_tiempo_serializer.save()
        
        return Response({"message": "Success", "control_tiempo": control_tiempo_serializer.data}, status=status.HTTP_201_CREATED) 
    
    def put(self, request, cliente_id, control_tiempo_id):
        try:
            control_tiempo = ControlTiempo.objects.get(id=control_tiempo_id, cliente=cliente_id)
        except ControlTiempo.DoesNotExist:
            return Response({"message": "No se encontró el registro de tiempo para el cliente con ID {}".format(cliente_id)},
                            status=status.HTTP_404_NOT_FOUND)

        control_tiempo_data = request.data
        control_tiempo_serializer = ControlTiempoSerializer(control_tiempo, data=control_tiempo_data, partial=True)

        if control_tiempo_serializer.is_valid():
            control_tiempo_serializer.save()
            return Response({"message": "Success", "control_tiempo": control_tiempo_serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response(control_tiempo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class GenereteDataClientesApiView(APIView):
    
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