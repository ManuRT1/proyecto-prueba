from django.shortcuts import render,redirect
from .models import Alumnos
from .forms import ComentarioContactoForm,FormArchivos
from .models import Comentario
from .models import ComentarioContacto, Archivos
from django.shortcuts import get_object_or_404
import datetime
from django.contrib import messages


# Create your views here.
def registros (request):
    alumnos=Alumnos.objects.all()
    return render(request,"registros/principal.html",{'alumnos':alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():#si los datos recibidos son correctos
            form.save()#inserta
            return render(request,'registros/contacto.html')
    form = ComentarioContactoForm()
    #si saale mal se va a reenviar al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form':form})    

def contacto(request):
    return render(request,"registros/contacto.html")



def consultarComentarios(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, 'registros/consultaComentarios.html', {'comentarios': comentarios})

def eliminarComentarioContacto(request,id, confirmacion='registros/confirmarEliminacion.html'):
    comentario=get_object_or_404(ComentarioContacto,id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/consultaComentarios.html",{'comentarios':comentarios})
    return render(request,confirmacion,{'object':comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    # Referenciamos que el elemento del formulario pertenece al comentario
    # ya existente
    if form.is_valid():
        form.save()  # si el registro ya existe, se modifica.
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/consultaComentarios.html",
                      {'comentarios': comentarios})
    # Si el formulario no es válido nos regresa al formulario para verificar
    # datos
    return render(request, "registros/editarComentario.html",
                  {'comentario': comentario})
       
def consultaComentarioIndividual(request,id):
    comentario=ComentarioContacto.objects.get(id=id)
    return render(request,"registros/EditarComentario.html",{'comentario':comentario})  



     
from .models import Alumnos

def consultas(request):
    alumnos = Alumnos.objects.all()
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})


def consultar1(request):
    alumnos = Alumnos.objects.filter(carrera='TI')
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})    


def consultar2(request):
    alumnos = Alumnos.objects.filter(carrera='TI').filter(turno="Matutino")
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})   

def consultar3(request):
    alumnos = Alumnos.objects.all().only('matricula','nombre','carrera','turno','imagen') 
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})  

def consultar4(request):
    alumnos = Alumnos.objects.filter(nombre__exact='Juan')
    return render(request, 'registros/consultas.html', {'alumnos': alumnos}) 

def consultar5(request):
    alumnos = Alumnos.objects.filter(matricula__regex='^UTM')
    return render(request, 'registros/consultas.html', {'alumnos': alumnos}) 

def consultar6(request):
    alumnos = Alumnos.objects.filter(nombre__in=["Juan","Ana"])
    return render(request,'registros/consultas.html',{'alumnos':alumnos})

def consultar7(request):
    fechaInicio = datetime.date(2002, 7,1 )
    fechaFin = datetime.date(2022, 7, 13)
    alumnos = Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,'registros/consultas.html',{'alumnos':alumnos})

def consultar8(request):
    alumnos = Alumnos.objects.filter(comentario__coment__contains='No inscrito')
    return render(request,'registros/consultas.html',{'alumnos':alumnos})

def consultasSQL(request):
    alumnos = Alumnos.objects.raw('SELECT id, matricula, nombre, carrera, turno,imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return render(request,'registros/consultas.html',{'alumnos':alumnos}) 

#ORM#
def consultarORM1(request):
    fechaInicio = datetime.date(2026, 6, 20)
    fechaFin = datetime.date(2026, 8, 4)
    comentarios = ComentarioContacto.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request, "registros/consultaComentarios.html", {'comentarios': comentarios})


def consultarORM2(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__icontains='mundo')
    return render(request, "registros/consultaComentarios.html", {'comentarios': comentarios})


def consultarORM3(request):
    comentarios = ComentarioContacto.objects.filter(usuario='Manuel2')
    return render(request, "registros/consultaComentarios.html", {'comentarios': comentarios})
    

#SQL#
def consultarSQL1(request):
    comentarios = ComentarioContacto.objects.raw(
        'SELECT id,usuario, mensaje, created FROM registros_comentariocontacto '
        'WHERE created BETWEEN "2026-06-20" AND "2026-08-04"'
    )  
    return render(request, "registros/consultaComentarios.html", {'comentarios': comentarios})
  

def consultarSQL2(request):
    comentarios = ComentarioContacto.objects.raw(
        'SELECT id,usuario,mensaje,created FROM registros_comentariocontacto '
        'WHERE mensaje LIKE "%mundo%"'
    )  
    return render(request, "registros/consultaComentarios.html", {'comentarios': comentarios})


def consultarSQL3(request):
    comentarios = ComentarioContacto.objects.raw(
    'SELECT id,usuario,mensaje,created FROM registros_comentariocontacto '
    'WHERE usuario="Manuel2"'    
    )
    return render(request, "registros/consultaComentarios.html", {'comentarios': comentarios})

def consultarSQL4(request):
    alumnos = Alumnos.objects.raw(
        'SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos '
        'WHERE nombre="Juan"'
    )
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})


def consultarSQL5(request):
    alumnos = Alumnos.objects.raw(
        'SELECT id, matricula, nombre, carrera, turno, imagen FROM registros_alumnos '
        "WHERE matricula GLOB 'UTM*'"
    )
    return render(request, 'registros/consultas.html', {'alumnos': alumnos})


def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST,request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion,archivo=archivo)
            insert.save()
            return redirect('Subir') 
        else:
            return render(request,"Error al procesar el formulario")
    else:
            return render(request,"registros/archivos.html",{'archivo':Archivos})
        
        
def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request, "registros/seguridad.html", {'nombre': nombre})      
        