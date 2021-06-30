from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Mandato, Usuario, Insumos

class MandatoForm(ModelForm):
    class Meta:
        model = Mandato
        fields = ['idMandato', 'montoMandato', 'numTarjeta',
                'fechaVencimiento', 'codigoVerificador', 'diaPago']
class Usuario (ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombreUsuario', 'correoUsuario', 'contraseñaUsuario',
                'tipoUsuario']

class InsumosForm (ModelForm):
    class Meta:
        model = Insumos
        fields= ['idInsumo','nombreInsumo','claseInsumo','costoInsumo','fechaVencimiento'] 