from django.shortcuts import get_object_or_404, render
from django.contrib import messages 
from .forms import FormArchivos
from .models import Archivos, Cabaña

def Catalogo(request):
    registros = Cabaña.objects.all()
    return render(request, 'registros/Catalogo.html', {'registros': registros})


def eliminarComentario(request, id, confirmacion = 'registros/ConfirmarElim.html'):
    comentario = get_object_or_404(Archivos, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = Archivos.objects.all()
        return render(request, 'registros/comentarios.html', {'comentarios': comentarios})
    return render(request, confirmacion, {'object': comentario})

def consultarComentario(request, id):
    comentario = Archivos.objects.get(id=id)
    return render(request, 'registros/editarCom.html', {'comentario': comentario})

# Editar
def editarComentario(request, id):
    comentario = get_object_or_404(Archivos, id=id)
    form = FormArchivos(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios = Archivos.objects.all()
        return render(request, 'registros/comentarios.html', {'comentarios': comentarios})
    return render(request, 'registros/comentarios.html', {'comentario':comentario })

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            nombre =request.POST['nombre']
            archivo =request.FILES['archivo']
            comentario =request.POST['comentario']
            archivoExp =request.FILES['archivoExp']
            insert = Archivos(nombre=nombre, archivo=archivo ,comentario=comentario ,archivoExp=archivoExp)
            insert.save()
            comentarios = Archivos.objects.all()
            return render(request, 'registros/comentarios.html', {'comentarios':comentarios})
        else:
            messages.error(request, 'Error al subir el archivo')
    else:
        return render(request, 'registros/comentarios.html', {'comentario':Archivos})

def consultasSQL(request):
    comentarios=Archivos.objects.raw('SELECT id, nombre, archivo, comentario, archivoExp FROM registros_archivos')
    return render (request, 'registros/comentarios.html', {'comentarios':comentarios})