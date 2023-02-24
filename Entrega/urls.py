from django.urls import path
from Entrega.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/", inicio, name="Start"),
    #path("agregar_profesor/", agregar_profesor,name="Agregar Profesor"),
    #path("ver_profesores/", ver_profesores,name="Ver Profesores"),
    #path("ver_estudiantes/", ver_estudiantes,name="Ver Estudiantes"),
    #path("ver_entregables/", ver_entregables,name="Ver Entregables"),
    #path("ver_cursos/", ver_cursos,name="Ver Cursos"),

    #path("crear_estudiantes/", crear_estudiantes,name="Crear Estudiantes"),
    #path("crear_cursos/", crear_cursos,name="Crear Cursos"),
    #path("crear_profesores/", crear_profesores,name="Crear Profesores"),
    #path("crear_entregables/", crear_entregables,name="Crear Entregables"),

    path("buscar_curso/", buscar_curso,name="Buscar Curso"),
    path("resultadoCurso/", resultado_curso,),

    path("buscar_profe/", buscar_profesor,name="Buscar Profesor"),
    path("resultadoProfe/", resultado_profe),

    path("buscar_estudiante/", buscar_estudiante,name="Buscar Estudiante"),
    path("resultadoEstudiante/", resultado_estudiante),

    path("buscar_entregable/", buscar_entregable,name="Buscar Entregable"),
    path("resultadoEntregable/", resultado_entregable),

    path("sobremi/", sobre_mi, name="Sobre Mi"),

    #path("borrar_profe/<profesor_nombre>",borrar_profesor,name="Borrar Profesor"),
    #path("editar_profe/<profesor_nombre>",editar_profesor,name="Editar Profesor"),

    #path("borrar_curso/<curso_nombre>",borrar_curso,name="Borrar Curso"),
    #path("editar_curso/<curso_nombre>",editar_curso,name="Editar Curso"),

    #path("borrar_estudiante/<estudiante_nombre>",borrar_estudiante,name="Borrar Estudiante"),
    #path("editar_estudiante/<estudiante_nombre>",editar_estudiante,name="Editar Estudiante"),

    #path("borrar_entregable/<entregable_nombre>",borrar_entregable,name="Borrar Entregable"),
    #path("editar_entregable/<entregable_nombre>",editar_entregable,name="Editar Entregable"),

    path("registro/",registro,name="Sign Up"),
    path("iniciar_sesion/",iniciar_sesion,name="Sign In"),

    path("cerrar_sesion/", LogoutView.as_view(template_name="Entrega/logout.html"), name="Logout"),

    path("curso/lista/", cursolista.as_view(), name="ver cursos"),
    path("crear/curso/lista/", crearCurso.as_view(), name="crear cursos"),
    path("borrar/curso/lista/<int:pk>", borrarCurso.as_view(), name="borrar cursos"),
    path("editar/curso/lista/<int:pk>", editarCurso.as_view(), name="editar cursos"),

    path("estudiante/lista/", estudiantelista.as_view(), name="ver estudiantes"),
    path("crear/estudiante/lista/", crearEstudiante.as_view(), name="crear estudiantes"),
    path("borrar/estudiante/lista/<int:pk>", borrarEstudiante.as_view(), name="borrar estudiantes"),
    path("editar/estudiante/lista/<int:pk>", editarEstudiante.as_view(), name="editar estudiantes"),

    path("profesor/lista/", profesorlista.as_view(), name="ver profesores"),
    path("crear/profesor/lista/", crearProfesor.as_view(), name="crear profesores"),
    path("borrar/profesor/lista/<int:pk>", borrarProfesor.as_view(), name="borrar profesores"),
    path("editar/profesor/lista/<int:pk>", editarProfesor.as_view(), name="editar profesores"),

    path("entregable/lista/", entregablelista.as_view(), name="ver entregables"),
    path("crear/entregable/lista/", crearEntregable.as_view(), name="crear entregables"),
    path("borrar/entregable/lista/<int:pk>", borrarEntregable.as_view(), name="borrar entregables"),
    path("editar/entregable/lista/<int:pk>", editarEntregable.as_view(), name="editar entregables"),
]