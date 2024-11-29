from django.shortcuts import render, redirect
from .models import Envio

# Vista para mostrar la lista de envíos
def inicio_vistaEnvio(request):
    losenvios = Envio.objects.all()
    return render(request, "gestionarEnvios.html", {"misenvios": losenvios})

# Vista para registrar un nuevo envío
def registrarEnvio(request):
    if request.method == "POST":
        id_sucursal = request.POST["txtid_sucursal"]
        nombre = request.POST["txtnombre"]
        direccion = request.POST["txtdireccion"]
        telefono = request.POST["txttelefono"]
        ciudad = request.POST["txtciudad"]
        estado = request.POST["txtestado"]
        codigo_postal = request.POST["txtcodigo_postal"]

        guardarenvio = Envio.objects.create(
            id_sucursal=id_sucursal,
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            ciudad=ciudad,
            estado=estado,
            codigo_postal=codigo_postal
        )
        return redirect("inicio_vistaEnvio")
    return render(request, "registrarEnvio.html")

# Vista para seleccionar y editar un envío
def seleccionarEnvio(request, id_sucursal):
    envio = Envio.objects.get(id_sucursal=id_sucursal)
    return render(request, "editarEnvio.html", {"misenvios": envio})

# Vista para editar un envío
def editarEnvio(request):
    if request.method == "POST":
        id_sucursal = request.POST["txtid_sucursal"]
        nombre = request.POST["txtnombre"]
        direccion = request.POST["txtdireccion"]
        telefono = request.POST["txttelefono"]
        ciudad = request.POST["txtciudad"]
        estado = request.POST["txtestado"]
        codigo_postal = request.POST["txtcodigo_postal"]

        envio = Envio.objects.get(id_sucursal=id_sucursal)
        envio.nombre = nombre
        envio.direccion = direccion
        envio.telefono = telefono
        envio.ciudad = ciudad
        envio.estado = estado
        envio.codigo_postal = codigo_postal
        envio.save()

        return redirect("inicio_vistaEnvio")
    return render(request, "editarEnvio.html")

# Vista para borrar un envío
def borrarEnvio(request, id_sucursal):
    envio = Envio.objects.get(id_sucursal=id_sucursal)
    envio.delete()
    return redirect("inicio_vistaEnvio")
