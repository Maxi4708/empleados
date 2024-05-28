from django.contrib import admin
from .models import Empleado, Habilidades

# Registro de modelos
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'id',
        'full_name',
    )
    def full_name(self, obj):
      return obj.first_name + ' ' + obj.last_name,
    search_fields = ('first_name',)
    list_filter = ('departamento', 'job', 'habilidades',)
    filter_horizontal = ('habilidades', )




admin.site.register(Empleado, EmpleadoAdmin)
