from django.db import models

# Create your models here.
class Articulo(models.Model):
    fecha = models.DateTimeField('año de publicacion')
    tipo = models.ForeignKey("TipoArticulo", on_delete=models.SET_NULL, null=True)
    #tipo = models.ForeignKey("TipoArticulo", on_delete=models.CASCADE)
    autor = models.TextField()
    titulo = models.CharField(max_length=250)
    nombre_publicacion = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.fecha) + " " + self.titulo

class TipoArticulo(models.Model):
    nombre = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre
    