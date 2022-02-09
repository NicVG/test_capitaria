from django.db import models

# Create your models here.
class Alumnos(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre_alumno = models.CharField(max_length=255)
    apellido_alumno = models.CharField(max_length=255)

    def __str__(self):
        return f'Rut: {self.rut} Nombre: {self.nombre_alumno} Apellido: {self.apellido_alumno}'


class Cursos(models.Model):
    nombre_curso = models.CharField(max_length=255)
    rut_prof_asig = models.ForeignKey('Profesores', models.DO_NOTHING, db_column='rut_prof_asig')

    def __str__(self):
        return f'{self.nombre_curso}'

class Notas(models.Model):
    rut_alumno = models.ForeignKey('Alumnos', models.DO_NOTHING, db_column='rut_alumno')
    codigo_curso = models.ForeignKey('Cursos', models.DO_NOTHING, db_column='codigo_curso')
    no_prueba = models.SmallIntegerField()
    nota = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return f'Alumno: {self.rut_alumno} | {self.codigo_curso} | Prueba no°: {self.no_prueba} | Nota: {self.nota}'

class Profesores(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre_prof = models.CharField(max_length=255)
    apellido_prof = models.CharField(max_length=255)

    def __str__(self):
        return f'Rut: {self.rut} Nombre: {self.nombre_prof} Apellido: {self.apellido_prof}'