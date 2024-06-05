from django.urls import path
from . import views

urlpatterns = [
    path('crearDestino/', views.crear_destino, name='crear_destino'), 
    path('listarDestino/', views.listar_destino, name='listar_destino'),
    path('editarDestino/', views.editar_destino, name='editar_destino' ),
    path('editarDestino/<int:id>/', views.editar_destino, name='editar_destino_id'),
    path('eliminarDestino/', views.eliminar_destino, name='eliminar_destino'),
]