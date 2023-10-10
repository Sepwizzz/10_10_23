# Los decoradores en Python son una característica poderosa y flexible que permite modificar o extender el comportamiento de una función o método sin modificar su código fuente. Los decoradores son funciones que toman otra función como argumento y devuelven una nueva función que generalmente agrega o modifica el comportamiento de la función original.

# Aquí hay una descripción más detallada del concepto de decoradores:

# Funciones de orden superior: En Python, las funciones son ciudadanos de primera clase, lo que significa que pueden ser pasadas como argumentos a otras funciones. Esto permite que las funciones sean tratadas como datos, lo que es fundamental para la implementación de decoradores.

# Sintaxis de decorador: Los decoradores se aplican utilizando el símbolo @ seguido del nombre de la función decoradora justo encima de la definición de la función que se va a decorar. Esto es lo que se llama una sintaxis de decorador. Aquí tienes un ejemplo:

# python
# Copy code
# @decorador
def funcion_a_decorar():
    pass
    # Código de la funciónç

# Funciones decoradoras: Las funciones decoradoras son funciones regulares de Python que toman como argumento la función que se va a decorar. Estas funciones pueden realizar acciones antes o después de llamar a la función original, modificar los argumentos o el valor de retorno, o realizar cualquier otro tipo de procesamiento deseado.

# Modificación de comportamiento: Los decoradores se utilizan comúnmente para modificar el comportamiento de las funciones. Por ejemplo, pueden utilizarse para medir el tiempo de ejecución de una función, validar argumentos, agregar registros, implementar la autenticación, la autorización, la memoria caché, etc.

# Ejemplo de decorador:

# python
# Copy code
def mi_decorador(funcion):
    def wrapper(*args, **kwargs):
        # Código a ejecutar antes de la función original
        resultado = funcion(*args, **kwargs)
        # Código a ejecutar después de la función original
        return resultado
    return wrapper

@mi_decorador
def funcion_a_decorar():
    print("Función decorada")

funcion_a_decorar()
# En este ejemplo, mi_decorador es una función decoradora que envuelve funcion_a_decorar en una función wrapper, lo que permite agregar código antes y después de la ejecución de funcion_a_decorar.

# En resumen, los decoradores en Python son una forma elegante de extender o modificar el comportamiento de las funciones o métodos sin modificar su código fuente directamente, lo que promueve la reutilización del código y la separación de preocupaciones.