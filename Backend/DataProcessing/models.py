from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=40, verbose_name="Nombre")
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Empresas"
        verbose_name = "Empresa"

from django.core.validators import MaxValueValidator, MinValueValidator
class Registro(models.Model):
    mes = models.PositiveIntegerField(
        verbose_name="Mes",
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    ProduccionTotal = models.IntegerField(verbose_name="Produccion Total")
    CantidadPiezasConFallas = models.IntegerField(verbose_name="Cantidad de piezas con fallas")
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Registros"
        verbose_name = "Registro"
