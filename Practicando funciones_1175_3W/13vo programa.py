print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Programa 13: Argumentos solo de palabras clave

def keyword_only(*, x):
    """Imprime un número que solo puede ser pasado como palabra clave."""
    print(x)

# Llamar a la función correctamente
keyword_only(x=3)  # Salida: 3
# keyword_only(3)  # Esto causaría un error
