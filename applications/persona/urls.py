from django.urls import path, include
from django.contrib import admin

# IMPORTO EL PAQUETE DE VISTA
from . import views
from .models import Empleado
from .views import ListAllEmpleados, SuccessView, ListByAreaEmpleado, ListEmpleadoByKword, ListHabilidadesEmpleado, PersonaDetailView, EmpleadoCreateView


# REGISTRO DE MI MODELO
from django.apps import AppConfig

class PersonaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "applications.persona"


app_name = 'persona_app'

urlpatterns = [
        path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
        path('listar-by-area/', views.ListByAreaEmpleado.as_view()),
        path('buscar-empleado/', views.ListEmpleadoByKword.as_view()),
        path('success/', views.SuccessView.as_view()),
        path('habilidades/', views.ListHabilidadesEmpleado.as_view()),
        path('ver-persona/<pk>', views.PersonaDetailView.as_view()), 
        path('add-empleado/', views.EmpleadoCreateView.as_view()),   
        path('success/', views.SuccessView.as_view(), name = 'correcto'), 
        path('update-empleado/<pk>/',views.EmpleadoUpdateView.as_view(), name = 'modificar_empleado'),
        path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name = 'eliminar_empleado')
        ]
