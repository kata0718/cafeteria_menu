from django.contrib import admin

from .models import Categoria, Producto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'precio', 'disponible', 'fecha_ingreso')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre', 'descripcion')
