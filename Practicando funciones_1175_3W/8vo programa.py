print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Programa 8: Valor predeterminado

def country_name(country="Norway"):
    """Imprime el país de origen. Usa 'Norway' como valor predeterminado."""
    print("I am from " + country)

# Llamar a la función con y sin argumento
country_name("Sweden")  # Salida: I am from Sweden
country_name()  # Salida: I am from Norway
