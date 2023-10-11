#KWARGS

def persona(nombre, edad, ciudad): #Crea la funcion persona donde recibe los kwargs o las variables que se van a tomar dentro de la funcion
    print(f"Nombre: {nombre}") #imprime junto con "Nombre: " lo que sea que vaya a entrar en la variable que esta dentro de los corchetes
    print(f"Edad: {edad}")  #imprime junto con "Edad: " lo que sea que vaya a entrar en la variable que esta dentro de los corchetes
    print(f"Ciudad: {ciudad}")  #imprime junto con "Ciudad: " lo que sea que vaya a entrar en la variable que esta dentro de los corchetes



#persona(nombre="Messi", edad=36, ciudad="Rosario")    #Invoca la funcion "persona" y añade las variables Nombre = "Messi" ETC 


def datospr(**kwargs): #Crea la funcion datospr recibiendo los kwargs
    producto = kwargs #Toma como producto las KWARGS
    return producto   #Retorna el producto

datos = {
    'Papas': 5000,              
    'Carne': 6000,              #Se crea el diccionario con los datos de los productos
    'Cebolla': 2000
}

datosnuevos = datospr(**datos) #Se crea la variable datos nuevos con la funcion y que reciba el diccionario de los datos

print(datosnuevos) #Imprime los datos



#ARGS

def suma(*args): #Crea la funcion suma
    resultado = 0 #Crea la variable resultado con 0
    for numero in args: #crea el bucle que repase lo que entra a la funcion
        resultado += numero #suma todo lo que entra en el bucle y lo añade a resultado
    return resultado #retorna resultado

#resultado = suma(1, 2, 3, 4, 5) #invoca la funcion de suma
# print(resultado)  # imprime el resultado de la suma


def promedio(*args): #Crea la funcion de promedio 
    if len(args) == 0: #si la cantidad de datos es 0 da como resultado 0
        return 0 #retorna 0
    return sum(args) / len(args) #suma lo que haya en los datos dados

# resultado = promedio(5, 10, 15, 20) #da los datos en los parentesis 
# print(resultado)  # imprimira el resultado
