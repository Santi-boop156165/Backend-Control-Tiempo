from django.urls import path
from .views import ControlApiView,TiempoApiView


urlpatterns = [
    path('clientes', ControlApiView.as_view(), name = 'listar_clientes'),
    path('clientes/<int:id>', ControlApiView.as_view(), name = 'procesar_clientes'),
    path('usuarios', TiempoApiView.as_view(), name = 'listar_tiempo'),
    path('usuarios/<int:id>', TiempoApiView.as_view(), name = 'procesar_tiempos'),
]
