print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Programa 16: Argumentos solo de palabras clave

def my_function(*, x):
    """Imprime un número que solo puede ser pasado como palabra clave."""
    print(x)

# Llamar a la función correctamente
my_function(x=3)  # Salida: 3
# my_function(3)  # Esto causaría un error
