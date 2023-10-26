from rest_framework import viewsets, status
from rest_framework import mixins, generics, views
from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, date
from rest_framework.views import APIView  # Import APIView from rest_framework

from .models import (
    Empresa,
    Registro
)
from .serializers import (
    EmpresaSerializer,
    RegistroSerializer,
)

class EmpresaListCreateView(generics.ListCreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    # permission_classes = [all]


class RegistroListCreateView(generics.ListCreateAPIView):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
    # permission_classes = [all]
    
    
    
    
@api_view(["GET"])
def RegistrosEmpresa(request, Empresa_id):
    if request.method == "GET":
        queryset = models.Registro.objects.filter(speciality__name=speciality_name)


        serializer = BudgetSerializer(queryset, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        return Response({"message": "Notificaciones agregada"})

    return Response(status=405)
