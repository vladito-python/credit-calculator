print()

# Para escribir en un archivo se utiliza la función write().

with open("ejemplo.txt", "w") as file: # Si el archivo se abre en modo "w" el contenido se sobreescribe.
    file.write("Hola qué tal?\n")
    file.write("Cambié el contenido, adiós\n")

with open("ejemplo.txt", "a") as file: # Si se abre en modo "a" se agrega contenido al final.
    file.write("Estoy agregando cosas\n")
    file.write("Nos vemos\n")
