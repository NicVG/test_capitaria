from django.forms import modelform_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection

# Create your views here.
from tablas.models import Alumnos, Profesores, Cursos, Notas


def crud(request):
    return render(request,'crud.html')

def crud_alumnos(request):
    alumnos = Alumnos.objects.order_by('nombre_alumno','apellido_alumno')
    return render(request,'crud_alumnos.html', {'alumnos':alumnos})

def crud_profesores(request):
    profesores = Profesores.objects.order_by('nombre_prof','apellido_prof')
    return render(request,'crud_profesores.html', {'profesores':profesores})

def crud_cursos(request):
    cursos = Cursos.objects.order_by('codigo')
    return render(request,'crud_cursos.html', {'cursos':cursos})

def crud_notas(request):
    notas = Notas.objects.order_by('no_prueba','codigo_curso','id')
    return render(request,'crud_notas.html', {'notas': notas})

def lista_promedios(request):
    sql = 'select rut_alumno,nombre_alumno,apellido_alumno,nombre_curso,avg(nota) as promedio\
    from tablas_notas as n\
    join tablas_cursos as cu on n.codigo_curso = cu.codigo\
    join tablas_alumnos as al on n.rut_alumno = al.rut\
    group by rut_alumno,nombre_alumno,apellido_alumno,nombre_curso\
    order by nombre_alumno,apellido_alumno'
    cursor = connection.cursor()
    cursor.execute(sql)
    promedios = cursor.fetchall()

    return render(request, 'lista_promedios.html',{'promedios':promedios})

def lista_rojos(request):
    sql = 'select rut_alumno,nombre_alumno,apellido_alumno\
    from(\
    select rut_alumno,nombre_alumno,apellido_alumno,nombre_curso,avg(nota) as promedio \
    from tablas_notas as n \
    join tablas_cursos as cu on n.codigo_curso = cu.codigo\
    join tablas_alumnos as al on n.rut_alumno = al.rut\
    group by rut_alumno,nombre_alumno,apellido_alumno,nombre_curso\
    having avg(nota) < 4) a\
    group by rut_alumno,nombre_alumno,apellido_alumno\
    having count(rut_alumno) > 1\
    order by nombre_alumno,apellido_alumno'
    cursor = connection.cursor()
    cursor.execute(sql)
    rojos = cursor.fetchall()

    return render(request, 'lista_rojos.html',{'rojos':rojos})


AlumnoForm = modelform_factory(Alumnos,exclude=[])

def nuevoAlumno(request):
    if request.method == 'POST':
        formaAlumno = AlumnoForm(request.POST)
        if formaAlumno.is_valid():
            formaAlumno.save()
            return redirect('crud_alumnos')
    else:
        formaAlumno = AlumnoForm()
    return render(request,'nuevo_alumno.html',{'formaAlumno':formaAlumno})

def editarAlumno(request,rut):
    alumno = get_object_or_404(Alumnos, pk=rut)
    if request.method == 'POST':
        formaAlumno = AlumnoForm(request.POST, instance=alumno)
        if formaAlumno.is_valid():
            formaAlumno.save()
            return redirect('crud_alumnos')
    else:
        formaAlumno = AlumnoForm(instance=alumno)
    return render(request,'editar_alumno.html',{'formaAlumno':formaAlumno})

def eliminarAlumno(request,rut):
    alumno = get_object_or_404(Alumnos, pk=rut)
    if alumno:
        alumno.delete()
    return redirect('crud_alumnos')


ProfesorForm = modelform_factory(Profesores,exclude=[])

def nuevoProfesor(request):
    if request.method == 'POST':
        formaProfesor = ProfesorForm(request.POST)
        if formaProfesor.is_valid():
            formaProfesor.save()
            return redirect('crud_profesores')
    else:
        formaProfesor = ProfesorForm()
    return render(request,'nuevo_profesor.html',{'formaProfesor':formaProfesor})

def editarProfesor(request,rut):
    profesor = get_object_or_404(Profesores, pk=rut)
    if request.method == 'POST':
        formaProfesor = ProfesorForm(request.POST, instance=profesor)
        if formaProfesor.is_valid():
            formaProfesor.save()
            return redirect('crud_profesores')
    else:
        formaProfesor = ProfesorForm(instance=profesor)
    return render(request,'editar_profesor.html',{'formaProfesor':formaProfesor})

def eliminarProfesor(request,rut):
    profesor = get_object_or_404(Profesores, pk=rut)
    if profesor:
        profesor.delete()
    return redirect('crud_profesores')


CursoForm = modelform_factory(Cursos,exclude=[])

def nuevoCurso(request):
    if request.method == 'POST':
        formaCurso = CursoForm(request.POST)
        if formaCurso.is_valid():
            formaCurso.save()
            return redirect('crud_cursos')
    else:
        formaCurso = CursoForm()
    return render(request,'nuevo_curso.html',{'formaCurso':formaCurso})

def editarCurso(request,codigo):
    curso = get_object_or_404(Cursos, pk=codigo)
    if request.method == 'POST':
        formaCurso = CursoForm(request.POST, instance=curso)
        if formaCurso.is_valid():
            formaCurso.save()
            return redirect('crud_cursos')
    else:
        formaCurso = CursoForm(instance=curso)
    return render(request,'editar_curso.html',{'formaCurso':formaCurso})

def eliminarCurso(request,codigo):
    curso = get_object_or_404(Cursos, pk=codigo)
    if curso:
        curso.delete()
    return redirect('crud_cursos')


NotaForm = modelform_factory(Notas,exclude=[])

def nuevaNota(request):
    if request.method == 'POST':
        formaNota = NotaForm(request.POST)
        if formaNota.is_valid():
            formaNota.save()
            return redirect('crud_notas')
    else:
        formaNota = NotaForm()
    return render(request,'nueva_nota.html',{'formaNota':formaNota})

def editarNota(request,id):
    nota = get_object_or_404(Notas, pk=id)
    if request.method == 'POST':
        formaNota = NotaForm(request.POST, instance=nota)
        if formaNota.is_valid():
            formaNota.save()
            return redirect('crud_notas')
    else:
        formaNota = NotaForm(instance=nota)
    return render(request,'editar_nota.html',{'formaNota':formaNota})

def eliminarNota(request,id):
    nota = get_object_or_404(Notas, pk=id)
    if nota:
        nota.delete()
    return redirect('crud_notas')