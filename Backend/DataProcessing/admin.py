from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

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
    list_display = ["nombre", "id"]


from django.db.models import Max
from django.contrib.auth.hashers import make_password
from import_export import resources, fields
from import_export.widgets import ManyToManyWidget
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
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

class RegistroAdmin(ImportExportActionModelAdmin):
    resource_class = RegistroResource
    list_display = ["mes", "ProduccionTotal","CantidadPiezasConFallas"]


admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(Registro,RegistroAdmin)