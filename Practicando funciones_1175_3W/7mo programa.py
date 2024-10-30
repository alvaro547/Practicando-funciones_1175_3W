print(" ")
print("Alvaro Campechano 3W")
print(" ")
# Programa 7: Argumentos arbitrarios de palabras clave

def print_name(**kwargs):
    """Imprime el apellido del niño usando argumentos de palabras clave."""
    print("His last name is " + kwargs["lname"])

# Llamar a la función usando argumentos de palabras clave
print_name(fname="Tobias", lname="Refsnes")  # Salida: His last name is Refsnes
