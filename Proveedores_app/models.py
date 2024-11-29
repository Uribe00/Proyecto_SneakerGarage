from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id_proveedor=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    telefono= models.IntegerField()
    producto=models.CharField(max_length=100)
    metodo_pago=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    direccion=models.CharField(max_length=100)
    fecha_ultimo_envio=models.DateField()
    id_sucursal=models.IntegerField()
    


    def __str__(self):
        return self.nombre