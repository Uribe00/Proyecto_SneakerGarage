from django.urls import path
from . import views

urlpatterns = [
    path("inicio_vistaPromocion", views.inicio_vistaPromocion, name="inicio_vistaPromocion"),
    path("registrarPromocion/", views.registrarPromocion, name="registrarPromocion"),
    path("seleccionarPromocion/<id_ventas>", views.seleccionarPromocion, name="seleccionarPromocion"),
    path("editarPromocion/", views.editarPromocion, name="editarPromocion"),
    path("borrarPromocion/<id_ventas>", views.borrarPromocion, name="borrarPromocion"),
]
