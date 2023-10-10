# las funciones pueden retornar un tipo de dato es decir se puede hacer una funcion que complemente otra
#  retornando el parametro que nececita la otra ella no sabe que es un funcion la que le entrega el dato 
# a la funcion solo le interesa tener un dato 


def cifra(palabra): #la funcion va a cifar y retona la litas donde se van a almacenar los numeros 
    numeros = []

    for caracter in palabra:
        valor = ord(caracter)
        numeros.append(valor)

    return numeros


# cifra("hola")

def decifra(numeros): # y esta fucion recibe un lista como parametro  y imprime la lita que entrega la funcion cifra() 
    cadena = ''.join(map(chr, numeros)) 
    print(numeros,"\n","-"*len(cadena))
    
    print (cadena) # imprime la lista y el descifrado
    
    

decifra(cifra("hola"))




