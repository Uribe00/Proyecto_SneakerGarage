from django.db import models

# Create your models here.
class Productos(models.Model):
    id_producto=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=100)
    precio=models.IntegerField()
    cantidad=models.PositiveSmallIntegerField()
    stock=models.CharField(max_length=100)
    marca=models.CharField(max_length=100)
    modelo=models.CharField(max_length=100)

    def __str__(self):
        return self.nombre