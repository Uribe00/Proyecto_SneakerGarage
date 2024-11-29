from django.urls import path
from cuenta_app import views

urlpatterns = [
    path("inicio_vistaMateria/", views.inicio_vistaMateria, name="inicio_vistaMateria"),  # Asegúrate de que la ruta termine con "/"
    path("registrarmateria/", views.registrarmateria, name="registrarmateria"),  # Nombre de vista corregido
    path("seleccionarmateria/<int:id_cuenta>/", views.seleccionarmateria, name="seleccionarmateria"),  # Corregido con el nombre correcto de la vista y el tipo de dato
    path("editarmateria/", views.editarmateria, name="editarmateria"),  # Nombre de vista corregido
    path("borrarmateria/<int:id_cuenta>/", views.borrarmateria, name="borrarmateria"),  # Corregido con el nombre correcto de la vista y el tipo de dato
]


