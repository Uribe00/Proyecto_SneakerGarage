from django.urls import path
from Empleados_app import views

urlpatterns = [
    path("inicio_vistaEmpleado", views.inicio_vistaEmpleado, name="inicio_vistaEmpleado"),
    path("registrarEmpleado/", views.registrarEmpleado, name="registrarEmpleado"),
    path("seleccionarEmpleado/<id_empleado>",views.seleccionarEmpleado,name="seleccionarEmpleado"),
    path("editarEmpleado/",views.editarEmpleado, name="editarEmpleado"),
    path("borrarEmpleado/<id_empleado>",views.borrarEmpleado, name="borrarEmpleado"),
    
]

