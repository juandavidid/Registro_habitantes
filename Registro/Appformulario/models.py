from django.db import models

# Create your models here.
''''


class Registro(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dirrecion = models.CharField(max_length=100)
    telefono = models.CharField(max_length =50)
    cedula = models.CharField(max_length =50)
    ciudad =models.CharField(max_length=50)

    # se retorna el nombre en el panel administrador
    def __str__(self):
        return self.nombre

    
'''
