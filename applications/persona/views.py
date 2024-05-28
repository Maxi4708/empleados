from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Empleado

class ListAllEmpleados(ListView):
    template_name = "persona/list_all.html"
    paginate_by = 4
    ordering = 'first_name'
    model = Empleado
    context_object_name = 'datos'
    

class SuccessView(TemplateView):
    template_name = "persona/success.html"

#Listar por area

class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    def get_queryset(self):
        lista = Empleado.objects.filter(departamento__name = 'AREA DE GERENCIA')
        return lista

#listar empleados por palabra clave

class ListEmpleadoByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'lista'

    def get_queryset(self):
        print('*************************************************')
        palabra_clave = self.request.GET.get("kword",'')
        print('============================>' , palabra_clave)
        lista = Empleado.objects.filter(first_name = palabra_clave)
        print('LISTA RESULTADO: ', lista)

        return lista
    
class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=3)
        return empleado.habilidades.all()
    

class PersonaDetailView(DetailView):
    model = Empleado
    template_name = 'persona/detail_persona.html'
    context_object_name = 'lista'

    #def get_queryset(self,**kwargs):
    #    context = super(PersonaDetailView,self).get_context_data(**kwargs)
    #    context['titulo']='Empleado del mes'
    #    return context


class SuccessView(TemplateView):
        template_name = "persona/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    #fields = ['first_name','last_name','job']
    #fields = ('__all__')

    fields = [
         'first_name',
         'last_name',
         'job',
         'departamento',
         'habilidades',
    ]
    success_url = reverse_lazy('persona_app:correcto')

    def form_valid(self, form):
         # logica de proceso
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save() 
        return super(EmpleadoCreateView, self).form_valid(form)

class SuccessView(TemplateView):
        template_name = "persona/success.html"

class EmpleadoUpdateView(UpdateView):
     model = Empleado
     template_name = "persona/update.html"
     fields = [
         'first_name',
         'last_name',
         'job',
         'departamento',
         'habilidades',
    ] 
     success_url = reverse_lazy('persona_app:correcto')


class EmpleadoDeleteView(DeleteView):
     model = Empleado
     template_name = "persona/delete.html"
     success_url = reverse_lazy('persona_app:correcto')