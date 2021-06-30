from django.db import models

# Create your models here.
class Mandato(models.Model):
    idMandato = models.CharField(max_length=50, primary_key=True, verbose_name="Id Mandato")
    montoMandato = models.CharField(max_length=50, verbose_name="Monto Mandato")
    numTarjeta = models.CharField(max_length=50, verbose_name="Numero de la tarjeta")
    fechaVencimiento = models.CharField(max_length=50, verbose_name="Fecha de vencimiento")
    codigoVerificador = models.CharField(max_length=50, verbose_name="Codigo verificador")
    diaPago = models.CharField(max_length=50, verbose_name="Dia de pago")
    def __str__(self):
        return self.idMandato

class Insumos(models.Model):
    idInsumo = models.CharField(max_lenght=50, primary_key=True, verbose_name="Id Insumos")
    nombreInsumo = models.CharField(max_lenght=50, verbose="Nombre Insumo")
    claseInsumo = models.Charfield(max_lenght=50, verbose="Clase Insumo")
    costoInsumo = models.CharField(max_length=50, verbose_name="Costo Insumo")
    fechaVencimiento = models.CharField(max_length=50, verbose_name="Fecha de vencimiento")
    def _str__(self):
        return self.idInsumo
