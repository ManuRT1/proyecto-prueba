from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForm
from .models import Comentario
from .models import ComentarioContacto

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
    comentarios = Comentario.objects.all()
    return render(request, 'registros/consultaComentarios.html', {'comentarios': comentarios})

def consultarComentarios(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, 'registros/consultaComentarios.html', {'comentarios': comentarios})