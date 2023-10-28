from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import resources
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

# Register your models here.

class EmpresaResource(resources.ModelResource):
    class Meta:
        model = Empresa
        fields = (
            "id",
            "nombre",
        )
        export_order = (
            "id",
            "nombre",
        )

class EmpresaAdmin(ImportExportActionModelAdmin):
    resource_class = EmpresaResource
    list_display = ["nombre","ProduccionTotal","CantidadPiezasOK","CantidadPiezasError","PiezasOK","PiezasError"]
    list_filter = (
        "nombre",
    )
    #ordering = ("-ProduccionTotal",)

    def CantidadPiezasOK(self, obj):
        produccion = Registro.objects.filter(empresa=obj).aggregate(
            total=models.Sum("ProduccionTotal")
        )["total"]
        fallas = Registro.objects.filter(empresa=obj).aggregate(
            total=models.Sum("CantidadPiezasConFallas")
        )["total"]
        if fallas is None:
            fallas = 0
        if produccion is None:
            produccion = 0
        stock = produccion - fallas
        return stock

    def CantidadPiezasError(self, obj):
        fallas = Registro.objects.filter(empresa=obj).aggregate(
            total=models.Sum("CantidadPiezasConFallas")
        )["total"]
        if fallas is None:
            fallas = 0
        return fallas
    
    def ProduccionTotal(self, obj):
        produccion = Registro.objects.filter(empresa=obj).aggregate(
            total=models.Sum("ProduccionTotal")
        )["total"]
        if produccion is None:
            produccion = 0
        return produccion

    def PiezasOK(self, obj):
        produccion = Registro.objects.filter(empresa=obj).aggregate(
            total=models.Sum("ProduccionTotal")
        )["total"]
        fallas = Registro.objects.filter(empresa=obj).aggregate(
            total=models.Sum("CantidadPiezasConFallas")
        )["total"]
        if fallas is None:
            fallas = 0
        if produccion is None:
            produccion = 0
        CantidadPiezasOK = produccion - fallas
        print(CantidadPiezasOK, produccion)
        try:
            PiezasOK = CantidadPiezasOK / produccion 
        except:
            PiezasOK = 0
        return PiezasOK
    
    def PiezasError(self, obj):
        produccion = Registro.objects.filter(empresa=obj).aggregate(
            total=models.Sum("ProduccionTotal")
        )["total"]
        fallas = Registro.objects.filter(empresa=obj).aggregate(
            total=models.Sum("CantidadPiezasConFallas")
        )["total"]
        if fallas is None:
            fallas = 0
        if produccion is None:
            produccion = 0
        CantidadPiezasOK = produccion - fallas
        PiezasOK = CantidadPiezasOK / produccion 
        try:
            PiezasOK = CantidadPiezasOK / produccion 
        except:
            PiezasOK = 0
        try:
            PiezasError= fallas / produccion
        except:
            PiezasError = 0
        return PiezasError

class RegistroResource(resources.ModelResource):
    id = resources.Field(column_name="Registro", attribute="id")
    mes = resources.Field(column_name="Mes", attribute="mes")
    ProduccionTotal = resources.Field(column_name="ProduccionTotal", attribute="ProduccionTotal")
    CantidadPiezasConFallas = resources.Field(column_name="CantidaPiezasConFallas", attribute="CantidadPiezasConFallas")
    empresa = Field(
        column_name='Empresa',
        attribute='empresa',
        widget=ForeignKeyWidget(model=Empresa, field='nombre'))

    class Meta:
        model = Registro
        fields = (
            "id",
            "empresa",
            "mes",
            "ProduccionTotal",
            "CantidadPiezasConFallas",
        )
        export_order = fields
    def before_import_row(self, row, **kwargs):
        empresa_name = row.get('Empresa')

        if empresa_name:
            empresa, created = Empresa.objects.get_or_create(nombre=empresa_name)

class RegistroAdmin(ImportExportActionModelAdmin):
    resource_class = RegistroResource
    list_display = ["id","mes", "empresa","ProduccionTotal","CantidadPiezasConFallas"]


admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(Registro,RegistroAdmin)