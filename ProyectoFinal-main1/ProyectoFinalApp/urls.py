from django.contrib import admin

from django.urls import path
from .views import *


urlpatterns = [
    path("", inicio, name="inicio"),
    path("cursos", cursos, name="cursos"),
    path("eventos",eventos, name= "eventos"),
    path("agregar", agregar, name= "agregar"),
    path(r"agregar_collar", agregar_collar , name= "agregar_collar"),
    path(r"agregar_comida", agregar_comida , name= "agregar_comida"),
    path(r"agregar_pipeta", agregar_pipeta , name= "agregar_pipeta"),
    path(r"buscar", buscar , name= "buscar"),
    
]
