from django.db import models

# Create your models here.
class departamento(models.Model):
    name = models.CharField('Nombre', max_length= 50, blank = True, null = True, editable=True)
    shor_name = models.CharField('Nombre Corto', max_length=20, unique=True)
    anulate = models.BooleanField('Anulado',default=False)

    class Meta:
        ordering = ['-name']
        

    def __str__(self):
        return str(self.id)+' - '+ self.name +' - '+ self.shor_name