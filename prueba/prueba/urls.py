"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from inicio import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_registros.registros,name="Principal"),
    path('nombre/',views.nombre, name="Nombre"),
    path('contacto/',views_registros.contacto,name="Contacto"),
    path('formulario/',views.formulario, name="Formulario"),
    path('ejemplo/',views.ejemplo,name="Ejemplo"),
    path('registrar/',views_registros.registrar,name="Registrar"),
    path('consultarComentarios/', views_registros.consultarComentarios, name='ConsultaComentarios'),
    path('eliminarComentario/<int:id>/',views_registros.eliminarComentarioContacto,name='Eliminar'),
    path('editarComentario/<int:id>/',views_registros.editarComentarioContacto,name='Editar'),
    path('EditarComentario/<int:id>/',views_registros.consultaComentarioIndividual,name='ConsultaIndividual'),
    path('consultas/',views_registros.consultas,name='Consultas'),
    path('consultas1/',views_registros.consultar1,name='Consultas'),
    path('consultas2/',views_registros.consultar2,name='Consultas2'),
    path('consultas3/',views_registros.consultar3,name='Consultas3'),
    path('consultas4/',views_registros.consultar4,name='Consultas4'),
    path('consultas5/',views_registros.consultar5,name='Consultas5'),
    path('consultas6/',views_registros.consultar6,name='Consultas6'),
    path('consultas7/',views_registros.consultar7,name='Consultas7'),
    path('consultas8/',views_registros.consultar8,name='Consultas8'),
    path('consultasSQL/',views_registros.consultasSQL,name='sql'),
    path('consultasSQL1/',views_registros.consultarSQL1,name='consultasSQL1'),
    path('consultasSQL2/',views_registros.consultarSQL2,name='consultasSQL2'),
    path('consultasSQL3/',views_registros.consultarSQL3,name='consultasSQL3'),
    path('consultasORM1/',views_registros.consultarORM1,name='consultasORM1'),
    path('consultasORM2/',views_registros.consultarORM2,name='consultasORM2'),
    path('consultasORM3/',views_registros.consultarORM3,name='consultasORM3'),
    path('consultasSQL4/',views_registros.consultarSQL4,name='consultasSQL4'),
    path('consultasSQL5/',views_registros.consultarSQL5,name='consultasSQL5'),
    path('subir',views_registros.archivos,name='Subir'),
    path('seguridad',views_registros.seguridad,name="Seguridad"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)