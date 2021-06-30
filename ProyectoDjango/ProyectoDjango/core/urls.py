from django.urls import path
from .views import index, ingresoSalida, mandatos, signInDonadores, signInFuncionarios, signUp, insumos, insumosVista, serviciosDonador,serviciosFuncionario, mandatosVista


urlpatterns = [
    path('', index, name='index'),
    path('ingresoSalida', ingresoSalida, name="ingresoSalida"),
    path('mandatos', mandatos, name="mandatos"),
    path('signInDonadores', signInDonadores, name="signInDonadores"),
    path('signInFuncionarios', signInFuncionarios, name="signInFuncionarios"),
    path('signUp', signUp, name="signUp"),
    path ('insumos', insumos, name="insumos"),
    path ('insumosVista', insumosVista, name="insumosVista"),
    path ('serviciosDonador', serviciosDonador, name="serviciosDonador"),
    path ('serviciosFuncionario', serviciosFuncionario, name="serviciosFuncionario"),
    path ('mandatosVista', mandatosVista, name="mandatosVista")




]