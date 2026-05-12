from django.db import models

class Cliente(models.Model):
    # (Mantenemos tu modelo de Cliente igual)
    codigo_bc = models.CharField(max_length=20, unique=True, verbose_name="Nº")
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    direccion_2 = models.CharField(max_length=255, blank=True, null=True)
    cif_nif = models.CharField(max_length=20, blank=True, null=True)
    alias = models.CharField(max_length=200, blank=True, null=True)
    saldo = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    saldo_periodo = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    departamento_code = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    cod_almacen = models.CharField(max_length=50, blank=True, null=True)
    centro_responsabilidad = models.CharField(max_length=50, blank=True, null=True)
    programa_code = models.CharField(max_length=50, blank=True, null=True)
    programa_filter = models.CharField(max_length=50, blank=True, null=True)
    bloqueado = models.CharField(max_length=20, blank=True, null=True)
    tarifa_kg = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.codigo_bc} - {self.nombre}"

# NUEVO MODELO DE ARTÍCULOS
class Articulo(models.Model):
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Nº")
    descripcion = models.CharField(max_length=255)
    unidad_medida = models.CharField(max_length=20, verbose_name="Unidad medida base")
    coste_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    descripcion_alias = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"