"""test_capitaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from inicio.views import inicio
from tablas.views import crud, crud_alumnos, crud_profesores, crud_cursos, crud_notas, lista_promedios, lista_rojos, \
    nuevoAlumno, editarAlumno, eliminarAlumno, nuevoProfesor, editarProfesor, eliminarProfesor, nuevoCurso, editarCurso, \
    eliminarCurso, nuevaNota, editarNota, eliminarNota

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio),
    path('crud/',crud),
    path('lista_promedios/',lista_promedios),
    path('lista_rojos/',lista_rojos),
    path('crud/crud_alumnos/',crud_alumnos,name='crud_alumnos'),
    path('crud/crud_profesores/',crud_profesores,name='crud_profesores'),
    path('crud/crud_cursos/',crud_cursos,name='crud_cursos'),
    path('crud/crud_notas/',crud_notas,name='crud_notas'),
    path('crud/crud_alumnos/nuevo_alumno',nuevoAlumno),
    path('crud/crud_alumnos/editar_alumno/<str:rut>',editarAlumno),
    path('crud/crud_alumnos/eliminar_alumno/<str:rut>',eliminarAlumno),
    path('crud/crud_profesores/nuevo_profesor',nuevoProfesor),
    path('crud/crud_profesores/editar_profesor/<str:rut>',editarProfesor),
    path('crud/crud_profesores/eliminar_profesor/<str:rut>',eliminarProfesor),
    path('crud/crud_cursos/nuevo_curso',nuevoCurso),
    path('crud/crud_cursos/editar_curso/<int:codigo>',editarCurso),
    path('crud/crud_cursos/eliminar_curso/<int:codigo>',eliminarCurso),
    path('crud/crud_notas/nueva_nota',nuevaNota),
    path('crud/crud_notas/editar_nota/<int:id>',editarNota),
    path('crud/crud_notas/eliminar_nota/<int:id>',eliminarNota),
]
