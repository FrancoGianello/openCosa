from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    anno = models.DateField()
    
    # Para llamar a las funciones no estaticas de la clase es imperativo poner el parametro (self)
    def __str__(self):
        return f"{self.nombre} ({self.anno})"


class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    # Para llamar a las funciones no estaticas de la clase es imperativo poner el parametro (self)
    def __str__(self):
        return f"{self.nombre} ({self.descripcion})"

class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    anno = models.DateField()
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True)
    equipos = models.ManyToManyField(Equipo)
    # Para llamar a las funciones no estaticas de la clase es imperativo poner el parametro (self)
    def __str__(self):
        return f"{self.nombre} ({self.genero}) es del año: {self.anno}"

