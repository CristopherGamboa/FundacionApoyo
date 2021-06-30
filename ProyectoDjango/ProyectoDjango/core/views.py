from django.shortcuts import render
from .models import Mandato, Insumos
from .forms import MandatoForm, Usuario, InsumosForm

# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def ingresoSalida(request):
    return render(request, 'core/ingresoSalida.html')

def serviciosDonador(request):
    return render (request, 'core/serviciosDonador.html')

def serviciosFuncionario(request):
    return render (request, 'core/serviciosFuncionario.html')

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

def insumos(request):
    datos = {
        'form': InsumosForm()
    }
    if request.method == 'POST':
        formulario = InsumosForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Datos guardados de manera correcta"
        else:
            formulario = InsumosForm()
            datos['mensaje'] = "Error"
    return render (request, "core/insumos.html", datos)

def insumosVista (request):
    insumos= Insumos.objects.all()
    datos={
        'insumos':insumos
    }
    return render(request, 'core/insumosVista.html', datos)

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

def mandatosVista (request):
    mandatos= Mandato.objects.all()
    datos={
        'mandatos':mandatos
    }
    return render(request, 'core/mandatosVista.html', datos)