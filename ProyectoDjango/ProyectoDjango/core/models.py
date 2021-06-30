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

class tipoUsuario(models.Model):
    idTipoUsuario = models.IntegerField(primary_key=True ,verbose_name="Id tipo de usuario") 
    tipoUsuario = models.CharField(max_length=50, verbose_name="Tipo usuario")
    def __str__(self):
        return self.tipoUsuario

class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=70, verbose_name="Nombre Usuario")
    correoUsuario= models.CharField(max_length=50, verbose_name="Correo")
    contraseñaUsuario= models.CharField(max_length=50, verbose_name="Contraseña")
    tipoUsuario = models.ForeignKey(tipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreUsuario

class Insumos(models.Model):
    idInsumo = models.CharField(max_length=50, primary_key=True, verbose_name="Id Insumos")
    nombreInsumo = models.CharField(max_length=50, verbose_name="Nombre Insumo")
    claseInsumo = models.CharField(max_length=50, verbose_name="Clase Insumo")
    costoInsumo = models.CharField(max_length=50, verbose_name="Costo Insumo")
    fechaVencimiento = models.CharField(max_length=50, verbose_name="Fecha de vencimiento")
    def __str__(self):
        return self.nombreInsumo