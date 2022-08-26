from django.shortcuts import render
from registros.models import Cabaña




def Ofertas(request):
    registros = Cabaña.objects.filter(EnOferta="Si")
    return render(request, 'inicio/principal.html', {'registros': registros})