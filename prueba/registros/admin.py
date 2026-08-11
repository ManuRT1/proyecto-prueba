from django.contrib import admin
from .models import Alumnos
from .models import Comentario

from .models import ComentarioContacto

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display=('matricula','nombre','carrera','turno','created')
    list_editable = ('turno',)
    search_fields = ('matricula','nombre','carrera','turno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turno')
    
    def get_readonly_fields(self, request, obj = ...):
        if request.user.groups.filter(name="usuarios").exists():
            return('matricula','carrera','turno')
        elif request.user.groups.filter(name="usuarios2").exists():
         return ('matricula', 'turno')
        else:
            return('created','updated') 
            
admin.site.register(Alumnos,AdministrarModelo)

class AdministrarComentarios(admin.ModelAdmin):
    list_display=('id','coment','alumno')
    search_fields=('id','created')
    date_hierarchy='created'
    readonly_fields=('created','id')
admin.site.register(Comentario,AdministrarComentarios)    
    
    

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)