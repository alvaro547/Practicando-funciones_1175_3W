print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Programa 12: Argumentos solo posicionales

def positional_only(x, /):
    """Imprime un número que solo puede ser pasado posicionalmente."""
    print(x)

# Llamar a la función correctamente
positional_only(5)  # Salida: 5
# posonlyitional_only(x=5)  # Esto causaría un error
