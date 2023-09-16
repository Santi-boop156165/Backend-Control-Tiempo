from django.urls import path
from .views import ControlApiView,TiempoApiView,ControlTiempoCreateView


urlpatterns = [
    path('clientes', ControlApiView.as_view(), name = 'listar_clientes'),
    path('clientes/<int:id>', ControlApiView.as_view(), name = 'procesar_clientes'),
    path('usuarios', TiempoApiView.as_view(), name = 'listar_tiempo'),
    path('usuarios/<int:id>', TiempoApiView.as_view(), name = 'procesar_tiempos'),
    path('control_tiempo', ControlTiempoCreateView.as_view(), name = 'crear_control_tiempo'),
    path('control_tiempo/<int:cliente_id>/', ControlTiempoCreateView.as_view(), name='procesar_control_tiempo'),
    path('control_tiempo/<int:cliente_id>/<int:control_tiempo_id>/', ControlTiempoCreateView.as_view(), name='actualizar_control_tiempo')



]
