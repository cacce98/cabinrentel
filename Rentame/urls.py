"""Rentame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from inicio import views
from registros import views as views_registros
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Ofertas, name='ofertas'),
    path('catalogo/', views_registros.Catalogo, name='Catalogo'),
    path('comentarios/', views_registros.archivos, name='comentarios'),
    path('archivos/', views_registros.archivos, name='archivos'),
    path('consultasSQL/', views_registros.consultasSQL, name='consultasSQL'),
    path('eliminar/<int:id>', views_registros.eliminarComentario, name='eliminar'),
    path('consultarComentario/<int:id>', views_registros.consultarComentario, name='consultarComentario'),
    path('editar/<int:id>', views_registros.editarComentario, name='editar'),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)