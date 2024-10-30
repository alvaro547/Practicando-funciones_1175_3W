print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Programa 6: Argumentos con palabras clave

def print_children(child1, child2, child3):
    """Imprime el nombre del hijo más joven usando argumentos con palabras clave."""
    print("The youngest child is " + child3)

# Llamar a la función usando argumentos de palabras clave
print_children(child1="Emil", child2="Tobias", child3="Linus")  # Salida: The youngest child is Linus
