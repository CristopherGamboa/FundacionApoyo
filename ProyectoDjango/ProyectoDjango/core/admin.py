from django.contrib import admin
from django.db.models import manager
from .models import Mandato, tipoUsuario, Usuario, Insumos
# Register your models here.
admin.site.register(Mandato)
admin.site.register(tipoUsuario)
admin.site.register(Usuario)
admin.site.register(Insumos)