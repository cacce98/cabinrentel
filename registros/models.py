from django.db import models

class Cabaña(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='Clave')
    nombre = models.CharField(max_length=50)
    costoDia = models.IntegerField(verbose_name='Costo por día')
    NumPer = models.IntegerField(verbose_name='Número de personas')
    NumCamas = models.IntegerField(verbose_name='Número de camas')
    Servicios = models.TextField()
    Ubicacion = models.CharField(max_length=50)
    EnOferta = models.CharField(max_length=50, default='No', verbose_name='¿En oferta?')
    imagen = models.ImageField(upload_to='fotos', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Cabaña'
        verbose_name_plural = 'Cabañas'
        ordering = ['id']
    def __str__(self):
        return self.nombre


class Archivos(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    nombre = models.CharField(null=True, max_length=50, verbose_name="Nombre")
    archivo = models.FileField(upload_to='archivos', null=True, blank=True, verbose_name="Foto de Perfil")
    comentario = models.TextField(null=True, verbose_name="Comentario")
    archivoExp = models.FileField(upload_to="archivos2", null=True, blank=True, verbose_name="Foto de experiencia")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"
        ordering = ["-created"]
        
        def __str__(self):
            return self.archivo