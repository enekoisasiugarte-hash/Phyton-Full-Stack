from django.contrib import admin
from .models import Cliente, Articulo

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('codigo_bc', 'nombre', 'tarifa_kg', 'activo')
    search_fields = ('nombre', 'codigo_bc')

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion', 'unidad_medida', 'coste_unitario')
    search_fields = ('codigo', 'descripcion', 'descripcion_alias')