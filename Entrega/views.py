from django.shortcuts import render
from django.http import HttpResponse
from Entrega.models import *
from Entrega.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):

    return render(request,"Entrega/inicio.html")

def sobre_mi(request):

    return render(request,"Entrega/sobremi.html")

'''
def agregar_profesor(request):

    profe = Profesor(nombre = "gustavo", apellido="lavalle", email="gustavo_lasrosas@hotmail.com", profesion="data enginner")
    profe.save()

    return HttpResponse("Agregamos un nuevo profesor")
'''

def registro (request):
    
    if request.method == 'POST':
        
        miformulario = RegistroFormulario(request.POST)
        
        if miformulario.is_valid():
            
            miformulario.save()

            return render(request,"Entrega/inicio.html")
    else:

        miformulario = RegistroFormulario()

    return render(request,"Entrega/registro.html",{"formulario1":miformulario})

def iniciar_sesion(request):

    if request.method == 'POST':
        
        miformulario = AuthenticationForm(request, data = request.POST)
        
        if miformulario.is_valid():
            
            usuario = miformulario.cleaned_data.get("username")
            contra = miformulario.cleaned_data.get("password")

            miUsuario = authenticate(username=usuario, password=contra)

            if miUsuario:

                login(request,miUsuario)
                mensaje = f"{miUsuario}"

                return render(request,"Entrega/inicio.html", {"mensaje":mensaje})
        
        else:

            mensaje = f"Error ingresaste mal los datos "

            return render(request,"Entrega/inicio.html", {"mensaje":mensaje})

    else:

        miformulario = AuthenticationForm()

    return render(request,"Entrega/login.html",{"formulario1":miformulario})

'''
def ver_estudiantes(request):

    estudiantes = Estudiante.objects.all()

    return render(request,"Entrega/verEstudiantes.html",{"estudiantes":estudiantes})
    
def ver_profesores(request):

    profesores = Profesor.objects.all()

    return render(request,"Entrega/verProfesores.html",{"profesores":profesores})

def ver_entregables(request):

    entregables = Entregable.objects.all()

    return render(request,"Entrega/verEntregables.html",{"entregables":entregables})

def ver_cursos(request):

    cursos = Curso.objects.all()

    return render(request,"Entrega/verCursos.html",{"cursos":cursos})


def crear_estudiantes(request):
          

          if request.method == 'POST':
      
            estudiante =  Estudiante(nombre = request.POST['nombre'],
                           apellido = request.POST['apellido'],
                           fechaNacimiento = request.POST['fechaNacimiento'] )
 
            estudiante.save()
 
            return render(request, "Entrega/inicio.html")
 
      



          return render(request,"Entrega/crearEstudiantes.html")


def crear_cursos(request):
    

    if request.method == 'POST':

        miformulario = CursoFormulario(request.POST)

        if miformulario.is_valid():

            infoDic = miformulario.cleaned_data

            curso1 = Curso(nombre = infoDic["nombre"],
                           camada = infoDic["camada"],
                           comision = infoDic["comision"])
            
            curso1.save()

            return render(request,"Entrega/inicio.html")

    else:

        miformulario = CursoFormulario()

    return render(request,"Entrega/crearCursos.html",{"formulario1":miformulario})


def crear_profesores(request):
    

    if request.method == 'POST':

        miformulario = ProfesorFormulario(request.POST)

        if miformulario.is_valid():

            infoDic = miformulario.cleaned_data

            profe1 = Profesor(nombre = infoDic["nombre"],
                              apellido = infoDic["apellido"],
                              email = infoDic["email"],
                              profesion = infoDic["profesion"])
            
            profe1.save()

            return render(request,"Entrega/inicio.html")

    else:

        miformulario = ProfesorFormulario()

    return render(request,"Entrega/crearProfesores.html",{"formulario1":miformulario})


def crear_entregables(request):
    

    if request.method == 'POST':

        miformulario = EntregableFormulario(request.POST)

        if miformulario.is_valid():

            infoDic = miformulario.cleaned_data

            entregable1 = Entregable(nombre = infoDic["nombre"],
                           fecha = infoDic["fecha"],
                           entregado = infoDic["entregado"])
            
            entregable1.save()

            return render(request,"Entrega/inicio.html")

    else:

        miformulario = EntregableFormulario()

    return render(request,"Entrega/crearEntregables.html",{"formulario1":miformulario})
'''


def buscar_curso(request):

    return render(request,"Entrega/busquedaCurso.html")

def resultado_curso(request):
    if request.method == "GET":
        camadabusqueda = request.GET["camada"]
        resultados = Curso.objects.filter(camada__icontains=camadabusqueda)

        return render(request,"Entrega/resultadoCurso.html",{"camada":camadabusqueda,"resultado":resultados})

    return render(request,"Entrega/resultadoCurso.html")

def buscar_profesor(request):

    return render(request,"Entrega/busquedaProfe.html")

def resultado_profe(request):
    if request.method == "GET":
        profesionbusqueda = request.GET["profesion"]
        resultados = Profesor.objects.filter(profesion__icontains=profesionbusqueda)

        return render(request,"Entrega/resultadoProfe.html",{"profesion":profesionbusqueda,"resultado":resultados})

    return render(request,"Entrega/resultadoProfe.html")

def buscar_estudiante(request):

    return render(request,"Entrega/busquedaEstudiante.html")

def resultado_estudiante(request):
    if request.method == "GET":
        nombrebusqueda = request.GET["nombre"]
        resultados = Estudiante.objects.filter(nombre__icontains=nombrebusqueda)

        return render(request,"Entrega/resultadoEstudiante.html",{"nombre":nombrebusqueda,"resultado":resultados})

    return render(request,"Entrega/resultadoEstudiante.html")

def buscar_entregable(request):

    return render(request,"Entrega/busquedaEntregable.html")

def resultado_entregable(request):
    if request.method == "GET":
        fechabusqueda = request.GET["fecha"]
        resultados = Entregable.objects.filter(fecha__icontains=fechabusqueda)

        return render(request,"Entrega/resultadoEntregable.html",{"fecha":fechabusqueda,"resultado":resultados})

    return render(request,"Entrega/resultadoEntregable.html")

'''
def borrar_profesor(request, profesor_nombre,):
    
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()

    return render(request, "Entrega/inicio.html")

def editar_profesor(request, profesor_nombre):
    

    profesor = Profesor.objects.get(nombre=profesor_nombre)

    if request.method == 'POST':

        miformulario = ProfesorFormulario(request.POST)

        if miformulario.is_valid():

            infoDic = miformulario.cleaned_data

            profesor.nombre=infoDic["nombre"]
            profesor.apellido=infoDic["apellido"]
            profesor.email=infoDic["email"]
            profesor.profesion=infoDic["profesion"]

            profesor.save()

            return render(request,"Entrega/inicio.html")

    else:

        miformulario = ProfesorFormulario(initial={"nombre":profesor.nombre,
                                                   "apellido":profesor.apellido,
                                                   "email":profesor.email,
                                                   "profesion":profesor.profesion,})

    return render(request,"Entrega/editarProfesores.html",{"formulario1":miformulario})

def borrar_curso(request, curso_nombre):
    
    curso = Curso.objects.get(nombre=curso_nombre)
    curso.delete()

    return render(request, "Entrega/inicio.html")

def editar_curso(request, curso_nombre):
    

    curso = Curso.objects.get(nombre=curso_nombre)

    if request.method == 'POST':

        miformulario = CursoFormulario(request.POST)

        if miformulario.is_valid():

            infoDic = miformulario.cleaned_data

            curso.nombre=infoDic["nombre"]
            curso.camada=infoDic["camada"]
            curso.comision=infoDic["comision"]
            

            curso.save()

            return render(request,"Entrega/inicio.html")

    else:

        miformulario = CursoFormulario(initial={"nombre":curso.nombre,
                                                   "camada":curso.camada,
                                                   "comision":curso.comision})

    return render(request,"Entrega/editarCursos.html",{"formulario1":miformulario})


def borrar_estudiante(request, estudiante_nombre):
    
    estudiante = Estudiante.objects.get(nombre=estudiante_nombre)
    estudiante.delete()

    return render(request, "Entrega/inicio.html")

def editar_estudiante(request, estudiante_nombre):
    

    estudiante = Estudiante.objects.get(nombre=estudiante_nombre)

    if request.method == 'POST':

        miformulario = EstudianteFormulario(request.POST)

        if miformulario.is_valid():

            infoDic = miformulario.cleaned_data

            estudiante.nombre=infoDic["nombre"]
            estudiante.apellido=infoDic["apellido"]
            estudiante.fechaNacimiento=infoDic["fechaNacimiento"]
            

            estudiante.save()

            return render(request,"Entrega/inicio.html")

    else:

        miformulario = EstudianteFormulario(initial={"nombre":estudiante.nombre,
                                                   "apellido":estudiante.apellido,
                                                   "fechaNacimiento":estudiante.fechaNacimiento})

    return render(request,"Entrega/editarEstudiante.html",{"formulario1":miformulario})

def borrar_entregable(request, entregable_nombre):
    
    entregable = Entregable.objects.get(nombre=entregable_nombre)
    entregable.delete()

    return render(request, "Entrega/inicio.html")

def editar_entregable(request, entregable_nombre):
    

    entregable = Entregable.objects.get(nombre=entregable_nombre)

    if request.method == 'POST':

        miformulario = EntregableFormulario(request.POST)

        if miformulario.is_valid():

            infoDic = miformulario.cleaned_data

            entregable.nombre=infoDic["nombre"]
            entregable.fecha=infoDic["fecha"]
            entregable.entregado=infoDic["entregado"]
            

            entregable.save()

            return render(request,"Entrega/inicio.html")

    else:

        miformulario = EntregableFormulario(initial={"nombre":entregable.nombre,
                                                   "fecha":entregable.fecha,
                                                   "entregado":entregable.entregado})

    return render(request,"Entrega/editarEntregable.html",{"formulario1":miformulario})
'''

class cursolista(ListView):
    model = Curso

class crearCurso(LoginRequiredMixin,CreateView):
    model = Curso
    fields=["nombre","camada","comision"]
    success_url = "/Entrega/curso/lista/"

class borrarCurso(LoginRequiredMixin,DeleteView):
    model = Curso
    success_url = "/Entrega/curso/lista/"   

class editarCurso(LoginRequiredMixin,UpdateView):
    model = Curso
    fields=["nombre","camada","comision"]
    success_url = "/Entrega/curso/lista/"

class estudiantelista(ListView):
    model = Estudiante

class crearEstudiante(LoginRequiredMixin,CreateView):
    model = Estudiante
    fields=["nombre","apellido","fechaNacimiento"]
    success_url = "/Entrega/estudiante/lista/"

class borrarEstudiante(LoginRequiredMixin,DeleteView):
    model = Estudiante
    success_url = "/Entrega/estudiante/lista/"   

class editarEstudiante(LoginRequiredMixin,UpdateView):
    model = Estudiante
    fields=["nombre","apellido","fechaNacimiento"]
    success_url = "/Entrega/estudiante/lista/"

class profesorlista(ListView):
    model = Profesor

class crearProfesor(LoginRequiredMixin,CreateView):
    model = Profesor
    fields=["nombre","apellido","email","profesion"]
    success_url = "/Entrega/profesor/lista/"

class borrarProfesor(LoginRequiredMixin,DeleteView):
    model = Profesor
    success_url = "/Entrega/profesor/lista/"  

class editarProfesor(LoginRequiredMixin,UpdateView):
    model = Profesor
    fields=["nombre","apellido","email","profesion"]
    success_url = "/Entrega/profesor/lista/" 

class entregablelista(ListView):
    model = Entregable

class crearEntregable(LoginRequiredMixin,CreateView):
    model = Entregable
    fields=["nombre","fecha","entregado"]
    success_url = "/Entrega/entregable/lista/"

class borrarEntregable(LoginRequiredMixin,DeleteView):
    model = Entregable
    success_url = "/Entrega/entregable/lista/"

class editarEntregable(LoginRequiredMixin,UpdateView):
    model = Entregable
    fields=["nombre","fecha","entregado"]
    success_url = "/Entrega/entregable/lista/"
