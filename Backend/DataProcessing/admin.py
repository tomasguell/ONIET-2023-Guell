from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources

# Register your models here.

# Clase de import-export de curso
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


# Clase de filtros y busqueda de Categoria
class EmpresaAdmin(ImportExportActionModelAdmin):
    resource_class = EmpresaResource
    list_display = ["nombre", "id"]


admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(Registro)