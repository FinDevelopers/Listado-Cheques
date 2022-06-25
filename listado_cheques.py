def read_cheque(file):
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
            
            
        print(chequesConFormato)
            

read_cheque('cheques.csv')


'''
[
    {
        "NroCheque" : 123213,
        "CodigoBanco" :
    },
    {

    },
    {

    }
]
'''