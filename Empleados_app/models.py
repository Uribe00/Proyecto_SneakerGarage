from django.db import models

class Empleado(models.Model):
    id_empleado = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    puesto = models.CharField(max_length=100)
    salario = models.DecimalField(max_digits=10, decimal_places=2)  # Asegúrate que salario sea numérico

    def __str__(self):
        return self.nombre
