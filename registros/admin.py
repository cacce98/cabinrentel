from typing import Sequence
from django.contrib import admin

from .models import Archivos, Cabaña

class AdministrarCabaña(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'costoDia', 'NumPer', 'NumCamas', 'Servicios', 'Ubicacion')
    list_filter = ('id', 'nombre', 'costoDia', 'NumPer', 'NumCamas', 'Servicios', 'Ubicacion')
    search_fields = ('id', 'nombre', 'costoDia', 'NumPer', 'NumCamas', 'Servicios', 'Ubicacion')
    list_per_page = 10
    list_editable: Sequence[str] = ('nombre', 'costoDia', 'NumPer', 'NumCamas', 'Servicios', 'Ubicacion')
    

admin.site.register(Cabaña, AdministrarCabaña)


class Comentarios(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'archivo', 'comentario', 'archivoExp', 'created')
    list_filter = ('id', 'nombre', 'archivo', 'comentario', 'archivoExp', 'created')
    search_fields = ('id', 'nombre', 'archivo', 'comentario', 'archivoExp', 'created')

admin.site.register(Archivos, Comentarios)

