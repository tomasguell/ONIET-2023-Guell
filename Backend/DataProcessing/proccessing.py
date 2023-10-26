# from django.shortcuts import render

# Create your views here.

import os
import pandas as pd

csv_filename = 'Datos-ONIET---Hoja-1.csv'
csv_directory = 'C:/Users/facun/OneDrive/Documentos/Extra Projects/ONIET-2023/ONIET-2023-Guell/Backend/DataProcessing'
csv_path = os.path.join(csv_directory, csv_filename)

df = pd.read_csv(csv_path, on_bad_lines='skip')

last_row = df.iloc[len(df)-1].to_dict()
print('--------------')
print('--------------')
print('--------------')

empresas = {}
for row in df.iloc:
    row = row.to_dict()
    try:
        empresas[row['Empresa']].append(row)
    except KeyError:
        empresas[row['Empresa']] = []

# for empresa in empresas:
#     print(empresas[empresa])

[{'Registro': 6, 'Empresa': 'Empresa 1', 'Mes': 2, 'ProduccionTotal': 602, 'CantidaPiezasConFallas': 48}, {'Registro': 11, 'Empresa': 'Empresa 1', 'Mes': 3, 'ProduccionTotal': 699, 'CantidaPiezasConFallas': 169}, {'Registro': 16, 'Empresa': 'Empresa 1', 'Mes': 4, 'ProduccionTotal': 809, 'CantidaPiezasConFallas': 96}, {'Registro': 21, 'Empresa': 'Empresa 1', 'Mes': 5, 'ProduccionTotal': 754, 'CantidaPiezasConFallas': 196}, {'Registro': 26, 'Empresa': 'Empresa 1', 'Mes': 6, 'ProduccionTotal': 744, 'CantidaPiezasConFallas': 154}]
[{'Registro': 7, 'Empresa': 'Empresa 2', 'Mes': 2, 'ProduccionTotal': 586, 'CantidaPiezasConFallas': 48}, {'Registro': 12, 'Empresa': 'Empresa 2', 'Mes': 3, 'ProduccionTotal': 649, 'CantidaPiezasConFallas': 119}, {'Registro': 17, 'Empresa': 'Empresa 2', 'Mes': 4, 'ProduccionTotal': 942, 'CantidaPiezasConFallas': 174}, {'Registro': 22, 'Empresa': 'Empresa 2', 'Mes': 5, 'ProduccionTotal': 515, 'CantidaPiezasConFallas': 162}, {'Registro': 27, 'Empresa': 'Empresa 2', 'Mes': 6, 'ProduccionTotal': 518, 'CantidaPiezasConFallas': 55}]
[{'Registro': 8, 'Empresa': 'Empresa 3', 'Mes': 2, 'ProduccionTotal': 533, 'CantidaPiezasConFallas': 154}, {'Registro': 13, 'Empresa': 'Empresa 3', 'Mes': 3, 'ProduccionTotal': 730, 'CantidaPiezasConFallas': 33}, {'Registro': 18, 'Empresa': 'Empresa 3', 'Mes': 4, 'ProduccionTotal': 588, 'CantidaPiezasConFallas': 132}, {'Registro': 23, 'Empresa': 'Empresa 3', 'Mes': 5, 'ProduccionTotal': 646, 'CantidaPiezasConFallas': 100}, {'Registro': 28, 'Empresa': 'Empresa 3', 'Mes': 6, 'ProduccionTotal': 660, 'CantidaPiezasConFallas': 52}]
[{'Registro': 9, 'Empresa': 'Empresa 4', 'Mes': 2, 'ProduccionTotal': 838, 'CantidaPiezasConFallas': 125}, {'Registro': 14, 'Empresa': 'Empresa 4', 'Mes': 3, 'ProduccionTotal': 944, 'CantidaPiezasConFallas': 22}, {'Registro': 19, 'Empresa': 'Empresa 4', 'Mes': 4, 'ProduccionTotal': 768, 'CantidaPiezasConFallas': 155}, {'Registro': 24, 'Empresa': 'Empresa 4', 'Mes': 5, 'ProduccionTotal': 621, 'CantidaPiezasConFallas': 82}, {'Registro': 29, 'Empresa': 'Empresa 4', 'Mes': 6, 'ProduccionTotal': 591, 'CantidaPiezasConFallas': 32}]
[{'Registro': 10, 'Empresa': 'Empresa 5', 'Mes': 2, 'ProduccionTotal': 956, 'CantidaPiezasConFallas': 113}, {'Registro': 15, 'Empresa': 'Empresa 5', 'Mes': 3, 'ProduccionTotal': 723, 'CantidaPiezasConFallas': 10}, {'Registro': 20, 'Empresa': 'Empresa 5', 'Mes': 4, 'ProduccionTotal': 930, 'CantidaPiezasConFallas': 13}, {'Registro': 25, 'Empresa': 'Empresa 5', 'Mes': 5, 'ProduccionTotal': 688, 'CantidaPiezasConFallas': 164}, {'Registro': 30, 'Empresa': 'Empresa 5', 'Mes': 6, 'ProduccionTotal': 574, 'CantidaPiezasConFallas': 32}]

# ranking de acuerdo al rendimiento de cada empresa.

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
    
    
print(empresas_proccessing)

exit()

Cantidad_de_Piezas_con_fallas
Producción_Total

Cantidad_Piezas_Ok = Producción_Total - Cantidad_de_Piezas_con_fallas
porcentaje_Piezas_Ok = Cantidad_Piezas_Ok / Producción_Total
porcentaje_Piezas_Error = Cantidad_de_Piezas_con_fallas / Producción_Total

# print(last_row)
# ranking = {
#     [
#     'Empresa',
#     'Producción Total',
#     'Cantidad Piezas Ok',
#     'Cantidad Piezas Error',
#     '%Piezas Ok',
#     '%Piezas Error'
#     ]
# }



