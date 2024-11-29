from django.shortcuts import render, redirect
from .models import Productos

# Create your views here.
def inicio_vistaProducto(request):
    losproductos = Productos.objects.all()
    return render(request, "gestionarProducto.html", {"misproductos": losproductos})

def registrarProducto(request):
    id_producto = request.POST["txtid_producto"]
    nombre = request.POST["txtnombre"]
    precio = request.POST["numprecio"]
    cantidad = request.POST["numcantidad"]
    stock = request.POST["txtstock"]
    marca = request.POST["txtmarca"]
    modelo = request.POST["txtmodelo"]

    guardarproducto = Productos.objects.create(
        id_producto=id_producto, nombre=nombre, precio=precio, cantidad=cantidad, stock=stock, marca=marca, modelo=modelo
    )

    return redirect("inicio_vistaProducto")

def seleccionarProducto(request, id_producto):
    losproductos = Productos.objects.get(id_producto=id_producto)
    return render(request, "editarProducto.html", {"misproductos": losproductos})

def editarProducto(request):
    id_producto = request.POST["txtid_producto"]
    nombre = request.POST["txtnombre"]
    precio = request.POST["numprecio"]
    cantidad = request.POST["numcantidad"]
    stock = request.POST["txtstock"]
    marca = request.POST["txtmarca"]
    modelo = request.POST["txtmodelo"]

    producto = Productos.objects.get(id_producto=id_producto)
    producto.nombre = nombre
    producto.precio = precio
    producto.cantidad = cantidad
    producto.stock = stock
    producto.marca = marca
    producto.modelo = modelo
    producto.save()

    return redirect("inicio_vistaProducto")

def borrarProducto(request, id_producto):
    producto = Productos.objects.get(id_producto=id_producto)
    producto.delete()
    return redirect("inicio_vistaProducto")
