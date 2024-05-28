from importlib.util import module_from_spec
from django.db import models
from applications.departamento.models import departamento
from ckeditor.fields import RichTextField

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    def __str__(self):
        return  self.habilidad



class Empleado(models.Model):

    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )

    first_name = models.CharField('Nombre', max_length=60)
    last_name = models.CharField('Apellido', max_length=60)
    
    full_name = models.CharField( 'Nombres Completos', max_length=120, blank=True )


    job = models.CharField('Trabajo', max_length=50, choices= JOB_CHOICES)
    departamento = models.ForeignKey(departamento,on_delete=models.CASCADE)
    image = models.ImageField('Imagen', upload_to=None, height_field=None, width_field= None, max_length=None)
    #avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    #hoja_vida = RichTextField(null = True)
 

    class Meta:
        
        ordering = ['-id', '-first_name', '-last_name']
       

    def __str__(self):
        return str(self.id)+',  '+self.first_name+',  '+self.last_name