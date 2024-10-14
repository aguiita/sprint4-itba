import argparse
import csv
import time
from datetime import datetime

def procesarcheques(dnicliente, tipocheque, estado=None, rangofecha=None):
    resultados=[]

    #abro el archivo csv
    with open('listado_cheques2.csv', mode='r') as archivo:
        lector=csv.DictReader(archivo)
        for linea in lector:
            # Filtrar por DNI
            if linea['DNI'] != dnicliente:
                continue
            
            # filtro por tipo de cheque
            if linea['TIPODECHEQUE'] != tipocheque:
                continue
            
            # Filtro por estado si es que hay

            if estado and linea['ESTADO'] != estado:
                continue
            
            # filtro por rango de fechas
            if rangofecha:
                # si no hay rango de fecha, el if no se hace.
                fechaorigen = datetime.fromtimestamp(int(linea['FechaOrigen']))
                # me fijo si el valor de fechaorigen cae dentro del rango de fechas q me da el rangofecha
                if not (rangofecha[0] <= fechaorigen <= rangofecha[1]):
                 continue

# 'Si se encuentra un número de cheque repetido en la misma cuenta para un DNI 
# dado, mostrar un mensaje de error indicando el problema'
            cuenta_origen = linea['NUMEROCUENTAORIGEN']
            nro_cheque = linea['NUMEROCHEQUE']
            if any(r['NUMEROCHEQUE'] == nro_cheque and r['NUMEROCUENTAORIGEN'] == cuenta_origen for r in resultados):
                    print(f"Error: El numero de cheque esta repetido ({nro_cheque}) para  {cuenta_origen}.")
            continue
       



 # cuando todos los filtros, agrega el cheque a resultados
        resultados.append(linea)
    return resultados

def exportar_a_un_csv(resultados,dnicliente):
    timestamp=int(time.time())
    nombre_archivo=f"{dnicliente}_{timestamp}.csv"
    with open (nombre_archivo, mode='w') as archivo:
        auxi=csv.DictWriter(archivo, fieldnames=resultados[0].keys())
        auxi.writeheader()
        auxi.writerows(resultados)
    print(f"Nuevo archivo exportado:{nombre_archivo}")    

vauxi = ''
while vauxi != 'no':
    dnicliente = input('Ingrese el DNI del cliente: ')
    tipocheque = input('Ingrese el tipo de cheque (EMITIDO/DEPOSITADO): ')
    estado = input('Ingrese el estado del cheque (opcional): ')
    
    # rango de fechas
    rangofechainput = input('Ingrese el rango de fechas YYYY-MM-DD:YYYY-MM-DD (opcional): ')
    rangofecha= None

    # Llama a la función de procesamiento
    resultados = procesarcheques (dnicliente, tipocheque, estado, rangofecha)

     # Muestro resultados o exporto  a un CSV
    if resultados:
        salida = input('¿desea ver los resultados en PANTALLA o exportarlos a CSV?: ').upper()
        if salida == 'PANTALLA':
            print("Resultados que se encontraron:")
            for resultado in resultados:
                print(resultado)
            #sino :
    
        elif salida == 'CSV':
            exportar_a_un_csv(resultados, dnicliente)
    else:
        print("No se encontraron cheques que coincidan .")


    vauxi = input('¿desea continuar ingresando datos? (si/no): ')
    
    # Muestro resultados
    print("Resultados encontrados:")
    for resultado in resultados:
        print(resultado)
