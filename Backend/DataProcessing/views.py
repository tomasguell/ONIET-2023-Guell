from rest_framework import viewsets, status
from rest_framework import mixins, generics, views
from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, date
from rest_framework.views import APIView  # Import APIView from rest_framework
from rest_framework.decorators import api_view
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

import json
from django.http import JsonResponse
import os
import pandas as pd

def dataProccessing(request):
    if request.method == 'GET':
        try:   
            # empresas = Empresa.objects.all()
            # registros = Registro.objects.all()
            
            try:
                csv_filename = 'Backend/DataProcessing/Datos-ONIET---Hoja-1.csv'

                df = pd.read_csv(csv_filename, on_bad_lines='skip')
            except FileNotFoundError:
                csv_filename = './DataProcessing/Datos-ONIET---Hoja-1.csv'

                df = pd.read_csv(csv_filename, on_bad_lines='skip')

            empresas = {}
            for row in df.iloc:
                row = row.to_dict()
                try:
                    empresas[row['Empresa']].append(row)
                except KeyError:
                    empresas[row['Empresa']] = []

            empresas_proccessing = {}

            for empresa in empresas:
                # print(empresas[empresa])
                Producción_Total = 0
                Cantidad_de_Piezas_con_fallas = 0
                for row in empresas[empresa]:
                    Producción_Total += row['ProduccionTotal']
                    Cantidad_de_Piezas_con_fallas += row['CantidaPiezasConFallas']
                
                
                Cantidad_Piezas_Ok = Producción_Total - Cantidad_de_Piezas_con_fallas
                porcentaje_Piezas_Ok = Cantidad_Piezas_Ok / Producción_Total
                porcentaje_Piezas_Error = Cantidad_de_Piezas_con_fallas / Producción_Total

                empresas_proccessing[empresa] = {}
                empresas_proccessing[empresa]['Producción_Total'] = Producción_Total
                empresas_proccessing[empresa]['Cantidad_Piezas_Ok'] = Cantidad_Piezas_Ok
                empresas_proccessing[empresa]['CantidaPiezasError'] = Cantidad_de_Piezas_con_fallas
                empresas_proccessing[empresa]['porcentaje_Piezas_Ok'] = porcentaje_Piezas_Ok
                empresas_proccessing[empresa]['porcentaje_Piezas_Error'] = porcentaje_Piezas_Error

            rows = []
            for emp in empresas_proccessing:
                index = {
                    'id': 1,
                    'Empresa' : emp,
                    'Produccion Total': empresas_proccessing[emp]["Producción_Total"],
                    'Cantidad Piezas Ok': empresas_proccessing[emp]["Cantidad_Piezas_Ok"],
                    'Cantidad Piezas Error': empresas_proccessing[emp]["CantidaPiezasError"],
                    '%Piezas Ok': empresas_proccessing[emp]["porcentaje_Piezas_Ok"],
                    '%Piezas Error': empresas_proccessing[emp]["porcentaje_Piezas_Error"],
                }
                rows.append(index)
                
            print(rows)

            return JsonResponse({'code': 'Success', 'msg': rows})
        except json.JSONDecodeError as e:
            return JsonResponse({'code': 'error', 'message': 'Invalid JSON data'})
    else:
        return JsonResponse({'code': 'error', 'message': 'Invalid request method'})
    

    
    
    
    
    
@api_view(["GET"])
def RegistrosEmpresa(request, Empresa_id):
    if request.method == "GET":
        queryset = Registro.objects.filter(empresa=Empresa_id)


        serializer = RegistroSerializer(queryset, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        return Response({"message": "Notificaciones agregada"})

    return Response(status=405)
