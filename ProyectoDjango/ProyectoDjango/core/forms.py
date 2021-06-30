from django import forms
from django.forms import ModelForm
from .models import Mandato, Insumos


class MandatoForm(ModelForm):
    model = Mandato 
    fields = ['idMandato', 'montoMandato', 'numTarjeta', 'fechaVencimiento', 'codigoVerificador', 'diaPago']

class InsumosForm(ModelForm):
    model = Insumos
    fields = ['idInsumo', 'nombreInsumo', 'claseInsumo', 'costoInsumo','fechaVencimiento ']
