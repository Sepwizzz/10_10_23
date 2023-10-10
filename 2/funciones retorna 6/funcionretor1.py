# Definimos una función llamada crear_calculadora que toma un operador como argumento
def crear_calculadora(operador):
    # Dentro de esta función, definimos una función interna llamada calcular
    def calcular(a, b):
        # Esta función interna realiza la operación deseada según el operador dado
        if operador == "+":
            return a + b
        elif operador == "-":
            return a - b
        elif operador == "*":
            return a * b
        elif operador == "/":
            if b != 0:
                return a / b
            else:
                return "Error: División por cero no permitida"
        else:
            return "Operador no válido"
    
    # Devolvemos la función interna calcular
    return calcular

# Usamos la función crear_calculadora para crear funciones específicas de cálculo
sumar = crear_calculadora("+")
restar = crear_calculadora("-")
multiplicar = crear_calculadora("*")
dividir = crear_calculadora("/")

# Ahora podemos usar las funciones creadas para realizar operaciones específicas
resultado_suma = sumar(10, 5)           # Suma: 10 + 5 = 15
resultado_resta = restar(20, 7)         # Resta: 20 - 7 = 13
resultado_multiplicacion = multiplicar(6, 4)  # Multiplicación: 6 * 4 = 24
resultado_division = dividir(8, 2)      # División: 8 / 2 = 4

# Imprimimos los resultados
print("Resultado de la suma:", resultado_suma)
print("Resultado de la resta:", resultado_resta)
print("Resultado de la multiplicación:", resultado_multiplicacion)
print("Resultado de la división:", resultado_division)
