from django.db import models

# Create your models here.
class materia(models.Model):
    id_cuenta=models.IntegerField(primary_key=True)
    id_usuario=models.IntegerField()
    nombre=models.CharField(max_length=100)
    contrasena=models.CharField(max_length=50)
    tipo_usuario=models.CharField(max_length=50)
    estado=models.CharField(max_length=50)
    fecha_creacion=models.DateField()


    def __str__(self):
        return self.id_cuenta