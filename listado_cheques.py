import sys
import os 
from datetime import datetime


# PASO 2 !!
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

if len(sys.argv) > 5:
    if len(sys.argv) > 6:
        estado = sys.argv[5] 
        fecha = sys.argv[6] 
    elif ':' in sys.argv[5]:
        estado = None
        fecha = sys.argv[5]
    else:
        estado = sys.argv[5]
        fecha = None
else:
    estado = None
    fecha = None


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
    print('No es un parámetro de estado válido')
    exit()

# Rango fecha: xx-xx-xxxx:yy-yy-yyyy
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
    desde = datetime(int(danho), int(dmes), int(ddia))
    hdia,hmes,hanho = hasta.split('-')
    hasta = datetime(int(hanho), int(hmes), int(hdia))

    if len(ddia) != 2 or len(dmes) != 2 or len(danho) !=4:
        print('Fecha desde no es correcta')
        exit()
    
    if len(hdia) != 2 or len(hmes) != 2 or len(hanho) !=4:
        print('Fecha hasta no es correcta')
        exit()
    
def get_cheques(file):
    with open(file, 'r') as archivo:
        cheques = csv.reader(archivo, delimiter=",")
        chequesConFormato = []
        for cheque in cheques:
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
        chequesConFormato.pop(0)
        return chequesConFormato

def filter_cheques(cheques):
    chequesFiltrados = []
    for cheque in cheques:
        if (int(cheque["DNI"]) == dni) and (cheque["Tipo"] == tipo) and (estado == None or cheque["Estado"] == estado):
            if(fecha != None):
                if(tipo == 'EMITIDO' and desde<=datetime.fromtimestamp(int(cheque['FechaOrigen']))<=hasta):
                    chequesFiltrados.append(cheque)
                elif(tipo == 'APROBADO' and desde<=datetime.fromtimestamp(int(cheque['FechaPago']))<=hasta):
                    chequesFiltrados.append(cheque)
            else:
                chequesFiltrados.append(cheque)

    return chequesFiltrados

def validar_cheques(cheques):
    array = []
    for cheque in cheques:
        array.append(str(cheque['NroCheque'])+str(cheque['NumeroCuentaOrigen']))
    if(len(set(array)) != len(array)):
        print('Error cheques repetidos')
        exit()

def print_cheques(cheques):
    for cheque in cheques:
        print ("----------------------------------------")   
        print ("CHEQUE")
        print (f'\tNUMERO DE CHEQUE: {cheque["NroCheque"]}')
        print (f'\tCODIGO DE BANCO: {cheque["CodigoBanco"]}')
        print (f'\tCODIGO DE SUCURSAL: {cheque["CodigoScurusal"]}')
        print (f'\tNUMERO DE CUENTA: {cheque["NumeroCuentaOrigen"]}')
        print (f'\tNUMERO DE CUENTA DESTINO: {cheque["NumeroCuentaDestino"]}')
        print (f'\tVALOR: {cheque["Valor"]}')
        print (f'\tFECHA ORIGEN: {cheque["FechaOrigen"]}')
        print (f'\tFECHA PAGO: {cheque["FechaPago"]}')
        print (f'\tDNI: {cheque["DNI"]}')
        print (f'\tTIPO DE CHEQUE: {cheque["Tipo"]}')
        print (f'\tESTADO: {cheque["Estado"]}')
    print ("----------------------------------------") 


def export_csv(cheques):
    with open (f"{dni}-{int(datetime.now().timestamp())}.csv", "w", newline='') as archivo:
        escribirArchivo = csv.writer(archivo)
        escribirArchivo.writerow(["NumeroCuentaOrigen","Valor","FechaOrigen","FechaPago"])
        for cheque in cheques:
            escribirArchivo.writerow([cheque["NumeroCuentaOrigen"], cheque["Valor"], cheque["FechaOrigen"], cheque["FechaPago"]])


def main(csv):
    cheques = get_cheques(csv)
    chequesFiltrados = filter_cheques(cheques)
    validar_cheques(chequesFiltrados)
    
    if salida == 'PANTALLA':
         print_cheques(chequesFiltrados)
    else:
         export_csv(chequesFiltrados)

main(archivo)


# COMANDOS PARA PROBAR
#python3 listado_cheques.py test.csv 233213214 PANTALLA EMITIDO
#py listado_cheques.py test.csv 11580999 CSV EMITIDO APROBADO 04-04-2021:04-05-2021 <_-- primer cheque 