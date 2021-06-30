from django.contrib import admin
from django.db.models import manager
from .models import Mandato, tipoUsuario, Usuario
# Register your models here.
admin.site.register(Mandato)
admin.site.register(tipoUsuario)
admin.site.register(Usuario)