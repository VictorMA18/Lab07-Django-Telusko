from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from .forms import *
from .models import *
# Create your views here.
def crear_destino(request):
    if request.method == 'POST':
        form = DestinoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Se guardo el destino") 
    else:
        form = DestinoForm()
    return render(request, '../templates/crear_destino.html', {'form': form})     

def listar_destino(request):
    destinos = DestinosTuristicos.objects.all()
    return render(request, '../templates/listar_destino.html', {'destinos': destinos})

def editar_destino(request, id=None):
    if id:
        destino = get_object_or_404(DestinosTuristicos, pk=id)
        if request.method == 'POST':
            form = DestinoForm(request.POST, request.FILES, instance=destino)
            if form.is_valid():
                form.save()
                return HttpResponse("Se edito el destino")
        else:
            form = DestinoForm(instance=destino)
    else:
        form = None

    destinos = DestinosTuristicos.objects.all()
    return render(request, '../templates/editar_destino.html', {'destinos': destinos, 'form': form , 'selected_destino': id})

def eliminar_destino(request):
    if request.method == 'POST':
        nombre_ciudad = request.POST.get('nombreCiudad')
        destinos = DestinosTuristicos.objects.filter(nombreCiudad=nombre_ciudad)
        if destinos.exists():
            destino = destinos.first() 
            destino.delete()
            return HttpResponse("Se eliminó el destino con éxito")
        else:
            return HttpResponseBadRequest("No se encontró ningún destino con el nombre de ciudad proporcionado")
    else:
        destinos = DestinosTuristicos.objects.all()
        return render(request, '../templates/eliminar_destino.html', {'destinos': destinos})