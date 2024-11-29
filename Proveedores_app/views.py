from django.shortcuts import render, redirect
from .models import Proveedor

# Create your views here.
def inicio_vistaProveedor(request):
    losproveedores=Proveedor.objects.all()
    return render(request,"gestionarProveedores.html",{"misproveedores":losproveedores})

def registrarProveedor(request):
    id_proveedor=request.POST["txtid_proveedor"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["numtelefono"]
    producto=request.POST["txtproducto"]
    metodo_pago=request.POST["txtmetodo_pago"]
    email=request.POST["txtemail"]
    direccion=request.POST["txtdireccion"]
    fecha_ultimo_envio=request.POST["txtfecha"]
    id_sucursal=request.POST["txtid"]
    guardarproveedor=Proveedor.objects.create(
        id_proveedor=id_proveedor,nombre=nombre,telefono=telefono,producto=producto,metodo_pago=metodo_pago,email=email, direccion=direccion, fecha_ultimo_envio=fecha_ultimo_envio, id_sucursal=id_sucursal
    )#Guarda el registro

    return redirect("inicio_vistaProveedor")
def seleccionarProveedor(request,id_proveedor):
    losproveedores=Proveedor.objects.get(id_proveedor=id_proveedor)
    return render(request,"editarProveedores.html", {"misproveedores":losproveedores})

def editarProveedor(request):
    id_proveedor=request.POST["txtid_proveedor"]
    nombre=request.POST["txtnombre"]
    telefono=request.POST["numtelefono"]
    producto=request.POST["txtproducto"]
    metodo_pago=request.POST["txtmetodo_pago"]
    email=request.POST["txtemail"]
    direccion=request.POST["txtdireccion"]
    fecha_ultimo_envio=request.POST["txtfecha"]
    id_sucursal=request.POST["txtid"]
    proveedor=Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.nombre=nombre
    proveedor.telefono=telefono
    proveedor.producto=producto
    proveedor.metodo_pago=metodo_pago
    proveedor.email=email
    proveedor.direccion=direccion
    proveedor.fecha_ultimo_envio=fecha_ultimo_envio
    proveedor.id_sucursal=id_sucursal
    proveedor.save()#guarda registro actualizado
    return redirect("inicio_vistaProveedor")


def borrarProveedor(request, id_proveedor):
    proveedor=Proveedor.objects.get(id_proveedor=id_proveedor)
    proveedor.delete() # borra el registro
    return redirect("inicio_vistaProveedor")

    
