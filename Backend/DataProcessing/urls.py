from django.urls import include, path
from rest_framework import routers
from .views import (
    EmpresaListCreateView,
    RegistroListCreateView,
    dataProccessing,
    RegistrosEmpresa
)

# router = routers.DefaultRouter()
# urlpatterns = router.urls + [
urlpatterns = [
    path(
        "EmpresaListCreateView/",
        EmpresaListCreateView.as_view(),
        name="EmpresaListCreateView",
    ),
    path(
        "RegistroListCreateView/",
        RegistroListCreateView.as_view(),
        name="RegistroListCreateView",
    ),
    path('dataProccessing/', dataProccessing, name='dataProccessing'),
    path(
        "RegistrosEmpresa/<int:Empresa_id>",
        RegistrosEmpresa,
        name="RegistrosEmpresa",
    ),
]
