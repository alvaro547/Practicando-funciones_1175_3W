print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Programa 20: Recursividad

def tri_recursion(k):
    """Función recursiva que suma números de k a 1."""
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\nRecursion Example Results")
tri_recursion(6)  # Salida: imprime la suma de 6 a 1
