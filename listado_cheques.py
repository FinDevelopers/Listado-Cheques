import csv
import sys
import os 


# PASO 2 !
if len(sys.argv) < 5:
    print('Hay que ingresar por lo menos 4 parámetros') 
    exit()
if len(sys.argv) > 8:
    print('Hay parámetros de más')
    exit()

archivo = sys.argv[1]
dni = sys.argv[2]
salida = sys.argv[3]
tipo = sys.argv[4]
estado = sys.argv[5] if len(sys.argv) > 5 else None
fecha = sys.argv[6] if len(sys.argv) > 6 else None


# PASO 3 !!
# PARA VERIFICAR SI EL ARCHIVO EXISTE
if not os.path.exists(archivo) or not os.path.isfile(archivo):
    print('El archivo no existe')
    exit()

try:
    dni = int(dni)
except ValueError:
    print('No es un dni válido')
    exit()

if salida not in ['PANTALLA','CSV']:
    print('No es un parámetro de salida válido')
    exit()

if tipo not in ['EMITIDO','DEPOSITADO']:
    print('No es un parámetro de tipo válido')
    exit()

if estado and estado not in ['PENDIENTE','APROBADO', 'RECHAZADO']:
    print('No es un parámetro de tipo válido')

if fecha:
    if len(fecha.split(':')) != 2:
        print('No es una fecha correcta')
        exit()
    desde,hasta = fecha.split(':')
    if len(desde) != 10 or len(desde.split('-')) != 3:
        print('Fecha desde no es correcta')
        exit()
    if len(hasta) != 10 or len(hasta.split('-')) != 3:
        print('Fecha hasta no es correcta')
        exit()
    ddia,dmes,danho = desde.split('-')
    hdia,hmes,hanho = hasta.split('-')

    if len(ddia) != 2 or len(dmes) != 2 or len(danho) !=4:
        print('Fecha desde no es correcta')
        exit()
    
    if len(hdia) != 2 or len(hmes) != 2 or len(hanho) !=4:
        print('Fecha hasta no es correcta')
        exit()
    


def get_cheques(file):
    with open(file, 'r') as archivo:
        cheques = archivo.read().splitlines()
        cheques.pop(0)
        chequesConFormato = []
        for l in cheques:
            cheque = l.split(',')
            chequesConFormato.append(
                {
                    "NroCheque" : cheque[0],
                    "CodigoBanco": cheque[1],
                    "CodigoScurusal" : cheque[2],
                    "NumeroCuentaOrigen" : cheque[3],                    
                    "NumeroCuentaDestino" : cheque[4],
                    "Valor" : cheque[5],
                    "FechaOrigen" : cheque[6],
                    "FechaPago" : cheque[7],
                    "DNI" : cheque[8],
                    "Tipo": cheque[9],
                    "Estado" : cheque[10]
                })
            
        return chequesConFormato
         


# [{---},{},{},{},{}]
#cheques[0]["NroCheque"] ==> '123456789'
#cheques[1]["NroCheque"] 
#cheques[2]

#cheque["NroCheque"]  ==> '123456789'

def print_cheques(cheques):
    for cheque in cheques:
        print ("----------------------------------------")   
        print ("CHEQUE")
        print (f'\tCUENTA: {cheque["NumeroCuentaOrigen"]}')
        print (f'\tVALOR: {cheque["Valor"]}')
        print (f'\tFECHA ORIGEN: {cheque["FechaOrigen"]}')
        print (f'\tFECHA PAGO: {cheque["FechaPago"]}')
    print ("----------------------------------------") 



def export_csv(cheques):
    with open ("nombreArchivo.csv", "w", newline='') as archivo:
        escribirArchivo = csv.DictWriter(archivo, cheques[0].keys())
        escribirArchivo.writeheader()
        for cheque in cheques:
            escribirArchivo.writerow(cheque)




def main(csv):
    cheques = get_cheques(csv)
    print_cheques(cheques)
    #export_csv(cheques)

main(archivo)

'''
-------------------
CHEQUE
    CUENTA: 
    VALOR: $1234.00
    FECHA ORIGEN:
    FECHA PAGO:
-------------------
'''

""" 
[
    {
        'NroCheque': '123456789', 
        'CodigoBanco': '100', 
        'CodigoScurusal': '300', 
        'NumeroCuentaOrigen': '1111111111', 
        'NumeroCuentaDestino': '2222222222', 
        'Valor': '532.1', 
        'FechaOrigen': '1633316400', 
        'FechaPago': '1664938800', 
        'DNI': '55555555', 
        'Estado': 'aprobado'
    }, 
    {
        'NroCheque': '987654321', 
        'CodigoBanco': '1', 
        'CodigoScurusal': '1', 
        'NumeroCuentaOrigen': '2222222222', 
        'NumeroCuentaDestino': '3333333333', 
        'Valor': '1000.00', 
        'FechaOrigen': '1633834800', 
        'FechaPago': '1634007600', 
        'DNI': '66666666', 
        'Estado': 'rechazado'
    }, 
    {
        'NroCheque': '404040404', 
        'CodigoBanco': '123', 
        'CodigoScurusal': '80', 
        'NumeroCuentaOrigen': '1000000000', 
        'NumeroCuentaDestino': '2000000000', 
        'Valor': '54341.42', 
        'FechaOrigen': '1585537200', 
        'FechaPago': '1589425200', 'DNI': '77777777', 
        'Estado': 'pendiente'
    }
]
 """