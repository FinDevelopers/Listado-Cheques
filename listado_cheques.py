def read_cheques(file):
    with open(file, 'r') as archivo:
        cheques = archivo.read().splitlines()
        cheques.pop(0)
        chequesConFormato = []
        for l in cheques:
            cheque = l.split(';')
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
                    "Estado" : cheque[9]
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



def main(csv):
    cheques = read_cheques(csv)
    print_cheques(cheques)

main('cheques.csv')

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