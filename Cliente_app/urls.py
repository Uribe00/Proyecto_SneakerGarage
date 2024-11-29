from django.urls import path
from . import views

urlpatterns = [
    path('gestionarCliente', views.gestionarCliente, name='gestionarCliente'),
    path('registrarCliente/', views.registrarCliente, name='registrarCliente'),
    path('editarCliente/<str:id_cliente>/', views.editarCliente, name='editarCliente'),
    path('borrarCliente/<str:id_cliente>/', views.borrarCliente, name='borrarCliente'),
]
