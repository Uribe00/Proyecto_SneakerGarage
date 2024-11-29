from django.shortcuts import render, redirect
from .models import materia

# Vista para mostrar todas las materias
def inicio_vistaMateria(request):
    lasmaterias = materia.objects.all()
    return render(request, "gestionarMateria.html", {"mismaterias": lasmaterias})

# Vista para registrar una nueva materia
def registrarmateria(request):
    if request.method == "POST":
        id_cuenta = request.POST["txtid_cuenta"]
        id_usuario = request.POST["txtid_usuario"]
        nombre= request.POST["txtnombre"]
        contrasena = request.POST["txtcontrasena"]
        tipo_usuario = request.POST["txttipo_usuario"]
        estado = request.POST["txtestado"]
        fecha_creacion = request.POST["txtfecha_creacion"]

        guardarmateria = materia.objects.create(
            id_cuenta=id_cuenta, 
            id_usuario=id_usuario,
            nombre=nombre, 
            contrasena=contrasena, 
            tipo_usuario=tipo_usuario,
            estado=estado, 
            fecha_creacion=fecha_creacion
        )

        return redirect("inicio_vistaMateria")  # Redirigir a la lista de materias

# Vista para editar una materia
def seleccionarmateria(request, id_cuenta):
    materia_obj = materia.objects.get(id_cuenta=id_cuenta)
    return render(request, "editarmateria.html", {"mismaterias": materia_obj})

# Vista para guardar los cambios en una materia
def editarmateria(request):
    if request.method == "POST":
        id_cuenta = request.POST["txtid_cuenta"]
        id_usuario = request.POST["txtid_usuario"]
        nombre = request.POST["txtnombre"]
        contrasena = request.POST["txtcontrasena"]
        tipo_usuario = request.POST["txttipo_usuario"]
        estado = request.POST["txtestado"]
        fecha_creacion = request.POST["txtfecha_creacion"]

        materia_obj = materia.objects.get(id_cuenta=id_cuenta)
        materia_obj.id_usuario = id_usuario
        materia_obj.nombre = nombre
        materia_obj.contrasena = contrasena
        materia_obj.tipo_usuario = tipo_usuario
        materia_obj.estado = estado
        materia_obj.fecha_creacion = fecha_creacion
        materia_obj.save()  # Guardar los cambios

        return redirect("inicio_vistaMateria")  # Redirigir a la lista de materias

# Vista para borrar una materia
def borrarmateria(request, id_cuenta):
    materia_obj = materia.objects.get(id_cuenta=id_cuenta)
    materia_obj.delete()  # Borrar la materia
    return redirect("inicio_vistaMateria")  # Redirigir a la lista de materias

