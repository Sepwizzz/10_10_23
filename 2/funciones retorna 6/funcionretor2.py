# Definimos una función llamada crear_conversor_moneda que toma una tasa de cambio
def crear_conversor_moneda(tasa_de_cambio):
    # Dentro de esta función, definimos una función interna llamada convertir
    def convertir(cantidad):
        # Esta función interna calcula y devuelve la cantidad convertida
        return cantidad * tasa_de_cambio
    
    # Devolvemos la función interna convertir
    return convertir

# Usamos la función crear_conversor_moneda para crear conversores de moneda específicos
dolares_a_euros = crear_conversor_moneda(0.85)  # Conversor de dólares a euros
euros_a_pesos = crear_conversor_moneda(20.0)   # Conversor de euros a pesos

# Ahora podemos usar los conversores de moneda creados para realizar conversiones
monto_en_dolares = 100
monto_en_euros = dolares_a_euros(monto_en_dolares)  # Convertir 100 dólares a euros
monto_en_pesos = euros_a_pesos(monto_en_euros)     # Convertir euros a pesos

# Imprimimos los resultados
print(f"{monto_en_dolares} dólares son equivalentes a {monto_en_euros} euros.")
print(f"{monto_en_euros} euros son equivalentes a {monto_en_pesos} pesos.")

