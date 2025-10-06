from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    marca= models.CharField(max_length=100)
    modelo= models.CharField(max_length=100)
    km= models.IntegerField()

    # es para el administrador
    def __str__(self):
        return f"{self.marca} {self.modelo} "