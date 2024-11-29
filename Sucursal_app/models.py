from django.db import models

# Create your models here.
class Envio(models.Model):
    id_sucursal=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    direccion= models.CharField(max_length=100)
    telefono=models.IntegerField()
    ciudad=models.CharField(max_length=100)
    estado=models.CharField(max_length=100)
    codigo_postal=models.CharField(max_length=100)
    

    def __str__(self):
        return self.estado