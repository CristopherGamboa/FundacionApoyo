from django.shortcuts import render
from .models import Mandato
from .forms import MandatoForm, Usuario

# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def ingresoSalida(request):
    return render(request, 'core/ingresoSalida.html')


def mandatos(request):
    datos = {
        'form': MandatoForm()
    }
    if request.method == 'POST':
        formulario = MandatoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados de manera correcta"
        else:
            formulario = MandatoForm()
            datos['mensaje'] = "Error"
    return render(request, 'core/mandatos.html', datos)


def signInDonadores(request):
    return render(request, 'core/signInDonadores.html')


def signInFuncionarios(request):
    return render(request, 'core/signInFuncionarios.html')


def signUp(request):
    datos = {
        'form': Usuario()
    }
    if request.method == 'POST':
        formulario = Usuario(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados de manera correcta"
        else:
            formulario = Usuario()
            datos['mensaje'] = "Error"
    return render(request, 'core/signUp.html', datos)
