from django.db import models

# Create your models here.
class Promocion(models.Model):
    id_ventas = models.IntegerField(primary_key=True)
    cantidad = models.CharField(max_length=100)
    precio_total= models.FloatField()  # Cambié de IntegerField a TextField para una mejor descripción
    venta_fecha= models.DateField()
    metodo_pago = models.CharField(max_length=50)
    

    def __str__(self):
        return self.id_ventas
