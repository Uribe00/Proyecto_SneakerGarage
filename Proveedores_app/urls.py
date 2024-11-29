from django.urls import path
from Proveedores_app import views

urlpatterns = [
    path("inicio_vistaProveedor", views.inicio_vistaProveedor, name="inicio_vistaProveedor"),
    path("registrarProveedor/", views.registrarProveedor, name="registrarProveedor"),
    path("seleccionarProveedor/<id_proveedor>",views.seleccionarProveedor,name="seleccionarProveedor"),
    path("editarProveedor/",views.editarProveedor, name="editarProveedor"),
    path("borrarProveedor/<id_proveedor>",views.borrarProveedor, name="borrarProveedor"),
    
]

