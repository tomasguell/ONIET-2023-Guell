from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=40, verbose_name="Nombre")
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Empresas"
        verbose_name = "Empresa"

class Registro(models.Model):
    mes = models.PositiveIntegerField(
        verbose_name="Mes",
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    ProduccionTotal = models.IntegerField(verbose_name="Produccion Total")
    CantidadPiezasConFallas = models.IntegerField(verbose_name="Cantidad de piezas con fallas")
    def __str__(self):
        return self.id

    class Meta:
        verbose_name_plural = "Registros"
        verbose_name = "Registro"
