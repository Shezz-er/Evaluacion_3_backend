from django.db import models
import datetime

class Vehiculos(models.Model):
    patente = models.CharField(max_length= 6, primary_key=True)
    numero_chasis = models.CharField(null=False, max_length=17, unique= True)
    marca = models.CharField(null=False, max_length=20)
    modelo = models.CharField(null=False, max_length=10)
    ultima_revision = models.DateField(null=False, default=datetime.date.today)
    proxima_revision = models.DateField(null=False, default=datetime.date.today)
    observaciones = models.CharField(max_length=200)

class Computadores(models.Model):

    numero_insumo = models.IntegerField(max_length= 6, primary_key=True)
    nombre  = models.CharField(null=False, max_length=50)
    fecha_adquisicion = models.DateField(null=False, default=datetime.date.today)
    marca = models.CharField(null=False, max_length=30)
    stock = models.IntegerField(null=False, max_length= 6)
    descripcion = models.CharField(null=False, max_length= 100)


class Oficina(models.Model):

    nro_articulo = models.IntegerField(max_length= 6, primary_key=True)
    nombre  = models.CharField(null=False, max_length=50)
    ubicacion = models.CharField(null=False, max_length=50)
    stock = models.IntegerField(null=False, max_length= 6)
    descripcion = models.CharField(null=False, max_length= 100)

class Usuario(models.Model):

    username = models.CharField(max_length= 25, primary_key=True)
    password  = models.CharField(null=False, max_length=40, unique= True)
    email = models.CharField(null=False, max_length=60)
    nombre = models.CharField(null=False, max_length= 60)
    perfil = models.IntegerField(null=False, max_length= 2)