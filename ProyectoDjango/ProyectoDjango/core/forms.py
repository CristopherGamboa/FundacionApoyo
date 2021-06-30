from django import forms
from django.forms import ModelForm
from .models import Mandato, Usuario

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