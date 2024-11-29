from django.shortcuts import render, redirect
from .models import Cliente

# Vista para gestionar clientes
def gestionarCliente(request):
    misclientes = Cliente.objects.all()
    return render(request, 'gestionarCliente.html', {'misclientes': misclientes})

# Vista para registrar un nuevo cliente
def registrarCliente(request):
    if request.method == 'POST':
        id_cliente = request.POST['txtid_cliente']
        nombre = request.POST['txtnombre']
        apellidos = request.POST['txtapellidos']
        email = request.POST['txtemail']
        telefono = request.POST['numtelefono']
        fecha_registro = request.POST['txtfecha_registro']
        direccion = request.POST['txtdireccion']

        # Crear el cliente en la base de datos
        Cliente.objects.create(
            id_cliente=id_cliente,
            nombre=nombre,
            apellidos=apellidos,
            email=email,
            telefono=telefono,
            fecha_registro=fecha_registro,
            direccion=direccion
        )
        return redirect('gestionarCliente')

    return render(request, 'registrarCliente.html')

# Vista para editar un cliente existente
def editarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    if request.method == 'POST':
        cliente.usuario = request.POST['txtnombre']
        cliente.apellidos = request.POST['txtapellidos']
        cliente.email = request.POST['txtemail']
        cliente.telefono = request.POST['numtelefono']
        cliente.fecha_registro = request.POST['txtfecha_registro']
        cliente.direccion = request.POST['txtdireccion']
        cliente.save()
        return redirect('gestionarCliente')

    return render(request, 'editarCliente.html', {'cliente': cliente})

# Vista para borrar un cliente
def borrarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect('gestionarCliente')
