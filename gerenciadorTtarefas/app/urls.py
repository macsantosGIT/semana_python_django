from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('Listar_tarefas/', listar_tarefas, name="listar_tarefas"),
]