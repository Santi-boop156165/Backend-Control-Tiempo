from django.urls import path
from .views import ControlApiView


urlpatterns = [
    path('clientes', ControlApiView.as_view(), name = 'listar_clientes'),
    path('clientes/<int:id>', ControlApiView.as_view(), name = 'procesar_clientes'),
]
