from django.contrib import admin

# Register your models here.
from .models import Articulo, TipoArticulo

admin.site.register(Articulo)
admin.site.register(TipoArticulo)
