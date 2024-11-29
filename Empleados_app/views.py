from django.shortcuts import render, redirect
from .models import Empleado

# Create your views here.
def inicio_vistaEmpleado(request):
    losempleados=Empleado.objects.all()
    return render(request,"gestionarEmpleado.html",{"misempleados":losempleados})

def registrarEmpleado(request):
    id_empleado=request.POST["txtid_empleado"]
    nombre=request.POST["txtnombre"]
    apellidos=request.POST["txtapellidos"]
    telefono=request.POST["txttelefono"]
    email=request.POST["txtemail"]
    puesto=request.POST["txtpuesto"]
    salario=request.POST["txtsalario"]

    guardarempleado=Empleado.objects.create(
        id_empleado=id_empleado,nombre=nombre,apellidos=apellidos,telefono=telefono,email=email,puesto=puesto,salario=salario
    )#Guarda el registro

    return redirect("inicio_vistaEmpleado")
def seleccionarEmpleado(request,id_empleado):
    losempleados=Empleado.objects.get(id_empleado=id_empleado)
    return render(request,"editarEmpleado.html", {"misempleados":losempleados})

def editarEmpleado(request):
    id_empleado=request.POST["txtid_empleado"]
    nombre=request.POST["txtnombre"]
    apellidos=request.POST["txtapellidos"]
    telefono=request.POST["txttelefono"]
    email=request.POST["txtemail"]
    puesto=request.POST["txtpuesto"]
    salario=request.POST["txtsalario"]
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    empleado.nombre=nombre
    empleado.apellidos=apellidos
    empleado.telefono=telefono
    empleado.email=email
    empleado.puesto=puesto
    empleado.salario=salario
    empleado.save()#guarda registro actualizado
    return redirect("inicio_vistaEmpleado")


def borrarEmpleado(request, id_empleado):
    empleado=Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete() # borra el registro
    return redirect("inicio_vistaEmpleado")

    
