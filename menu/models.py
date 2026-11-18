from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    """Modelo PADRE clasificador. Se gestiona solo desde Django Admin."""
    nombre = models.CharField(max_length=60, unique=True)
    descripcion = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    """Modelo HIJO operativo. CRUD público con CBVs."""
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name='productos',
    )
    nombre = models.CharField(max_length=100)                      # texto
    descripcion = models.TextField(blank=True)                     # texto largo
    precio = models.DecimalField(max_digits=8, decimal_places=0)   # numérico
    fecha_ingreso = models.DateField(default=timezone.localdate)   # fecha
    disponible = models.BooleanField(default=True)                 # booleano

    class Meta:
        ordering = ['categoria__nombre', 'nombre']

    def __str__(self):
        return f'{self.nombre} ({self.categoria})'
