print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Programa 5: Argumentos arbitrarios

def print_kids(*kids):
    """Imprime el nombre del hijo más joven."""
    print("The youngest child is " + kids[2])

# Llamar a la función con múltiples argumentos
print_kids("Emil", "Tobias", "Linus")  # Salida: The youngest child is Linus
