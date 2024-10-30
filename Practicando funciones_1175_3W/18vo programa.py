print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Programa 18: Argumentos solo de palabras clave y error

def my_function(*, x):
    """Imprime un número que solo puede ser pasado como palabra clave."""
    print(x)

# my_function(3)  # Esto causaría un error
my_function(x=3)  # Llamar correctamente como palabra clave
