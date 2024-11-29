from django.db import models

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50, default="No Apellido")
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=15)  # Cambiado a CharField
    fecha_registro = models.DateField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
