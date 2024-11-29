from django.shortcuts import render, redirect
from .models import Promocion

# Create your views here.
def inicio_vistaPromocion(request):
    laspromociones = Promocion.objects.all()
    return render(request, "gestionarPromociones.html", {"mispromociones": laspromociones})

def registrarPromocion(request):
    id_ventas = int(request.POST["txtid_ventas"])  
    cantidad = request.POST["txtcantidad"]
    precio_total = request.POST["txtprecio_total"]
    venta_fecha = request.POST["txtventa_fecha"]
    metodo_pago = request.POST["txtmetodo_pago"]

    guardarpromocion = Promocion.objects.create(
        id_ventas=id_ventas,
        cantidad=cantidad,
        precio_total=precio_total,
        venta_fecha=venta_fecha,
        metodo_pago=metodo_pago,
    )  # Guarda el registro

    return redirect("inicio_vistaPromocion")

def seleccionarPromocion(request, id_ventas):
    laspromociones = Promocion.objects.get(id_ventas=id_ventas)
    return render(request, "editarPromociones.html", {"mispromociones": laspromociones})

def editarPromocion(request):
    id_ventas = request.POST["txtid_ventas"]
    cantidad = request.POST["txtcantidad"]
    precio_total = request.POST["txtprecio_total"]
    venta_fecha = request.POST["txtventa_fecha"]
    metodo_pago = request.POST["txtmetodo_pago"]


    promocion = Promocion.objects.get(id_ventas=id_ventas)
    promocion.cantidad = cantidad
    promocion.precio_total = precio_total
    promocion.venta_fecha = venta_fecha
    promocion.metodo_pago = metodo_pago
    promocion.save()  # Guarda el registro actualizado

    return redirect("inicio_vistaPromocion")

def borrarPromocion(request, id_ventas):
    promocion = Promocion.objects.get(id_ventas=id_ventas)
    promocion.delete()  # Borra el registro
    return redirect("inicio_vistaPromocion")
