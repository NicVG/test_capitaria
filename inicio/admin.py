from django.contrib import admin

# Register your models here.
from tablas.models import Alumnos, Profesores, Cursos, Notas

admin.site.register(Alumnos)
admin.site.register(Profesores)
admin.site.register(Cursos)
admin.site.register(Notas)

