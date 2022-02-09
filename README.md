Tablas

Tabla alumnos:
rut (var(10) PrimaryKey)
nombre_alumno (var)
apellido_alumno (var)

Tabla profesores:
rut (var(10) PrimaryKey)
nombre_prof (var)
apellido (var)

Tabla cursos:
codigo (int PrimaryKey)
nombre_curso (var)
rut_prof_asignado (var(10)) <- ForeignKey de tabla_profesores.rut

Tabla notas:
id (int PrimaryKey)
rut_alumno (var(10)) <- ForeignKey de tabla_alumnos.rut
codigo_curso (smallint) <- ForeignKey de tabla_cursos.codigo
no_prueba (smallint)
nota (smallint)




SQL

Pregunta 1:

select distinct rut_alumno,nombre_alumno,apellido_alumno
from notas as n 
join cursos as cu on n.codigo_curso = cu.codigo
join alumnos as al on n.rut_alumno = al.rut
where cu.nombre_curso = 'programación'


Pregunta 2:

select rut_alumno,nombre_alumno,apellido_alumno,nombre_curso,avg(nota) as promedio
from notas as n 
join cursos as cu on n.codigo_curso = cu.codigo
join alumnos as al on n.rut_alumno = al.rut
where rut_alumno = 'xxxxxxx' and nombre_curso = 'xxxxxx'
group by rut_alumno,nombre_alumno,apellido_alumno,nombre_curso

(en vez de rut_alumno se puede usar nombre_alumno and apellido_alumno para buscar a un alumno en específico)


Pregunta 3:

select rut_alumno,nombre_alumno,apellido_alumno,nombre_curso,avg(nota) as promedio
from notas as n 
join cursos as cu on n.codigo_curso = cu.codigo
join alumnos as al on n.rut_alumno = al.rut
group by rut_alumno,nombre_alumno,apellido_alumno,nombre_curso
order by nombre_alumno,apellido_alumno

(si se quiere ver más específicamente los promedios de todos los cursos de una sola persona se debe usar un where con el rut, o el nombre más el apellido como en el query anterior)


Pregunta 4:

select rut_alumno,nombre_alumno,apellido_alumno
from(
select rut_alumno,nombre_alumno,apellido_alumno,nombre_curso,avg(nota) as promedio 
from notas as n 
join cursos as cu on n.codigo_curso = cu.codigo
join alumnos as al on n.rut_alumno = al.rut
group by rut_alumno,nombre_alumno,apellido_alumno,nombre_curso
having avg(nota) < 4) a
group by rut_alumno,nombre_alumno,apellido_alumno
having count(rut_alumno) > 1
order by nombre_alumno,apellido_alumno

Pregunta 5:

b) 190 (sumatoria de 1 hasta 19)




DJango

Para el proyecto Django ya se deben haber cargado bases de datos o generar los models y realizar la migracion.
Se necesita instalar psycopg2 para poder realizar los query que manejan los view para imprimir en los template.
