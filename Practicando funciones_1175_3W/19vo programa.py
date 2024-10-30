print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Programa 19: Combinar solo posicional y solo de palabras clave

def my_function(a, b, /, *, c, d):
    """Suma de argumentos posicionales y de palabras clave."""
    print(a + b + c + d)

# Llamar a la función con argumentos posicionales y de palabras clave
my_function(5, 6, c=7, d=8)  # Salida: 26
