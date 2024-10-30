print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Programa 15: Argumentos solo posicionales

def my_function(x, /):
    """Imprime un número que solo puede ser pasado posicionalmente."""
    print(x)

# Llamar a la función correctamente
my_function(3)  # Salida: 3
# my_function(x=3)  # Esto causaría un error
