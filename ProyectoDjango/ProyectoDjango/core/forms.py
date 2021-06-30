from django import forms
from django.forms import ModelForm
from .models import Mandato

class MandatoForm(ModelForm):
    model = Mandato 
    fields = ['idMandato', 'montoMandato', 'numTarjeta', 'fechaVencimiento', 'codigoVerificador', 'diaPago']