import argparse
import csv
import time
from datetime import datetime
vauxi=''

def procesarcheques(dnicliente, tipocheque, estado=None, rangofecha=None):
    cheques=[]

    #abro el archivo csv
    with open('listado_cheques.cvs', mode='r') as archivo:
        lector=csv.DictReader(archivo)
    for linea in lector:
        # Filtrar por DNI
        if linea['DNI'] == dnicliente:
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
   


vauxi = ''
while vauxi != 'no':
    archivocsv = input('Ingrese el nombre del archivo CSV: ')
    dnicliente = input('Ingrese el DNI del cliente: ')
    tipocheque = input('Ingrese el tipo de cheque (EMITIDO/DEPOSITADO): ')
    estado = input('Ingrese el estado del cheque (opcional): ')
    
    # rango de fechas
    rangofechainput = input('Ingrese el rango de fechas YYYY-MM-DD:YYYY-MM-DD (opcional): ')
    rangofecha= None

    vauxi = input('¿desea continuar ingresando datos? (si/no): ')
    
    # Llama a la función de procesamiento
    resultados = procesarcheques(archivocsv, dnicliente, tipocheque, estado, rangofecha)
    
    # Muestro resultados
    print("Resultados encontrados:")
    for resultado in resultados:
        print(resultado)
