from django.db import models

# Create your models here.

class Prueba(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=70)
    cantidad = models.IntegerField()

    def __str__(self):
        return  str(self.id)+ '. '+self.titulo+ ' '+ str(self.cantidad)+ ' - '+self.subtitulo+'.'
        


