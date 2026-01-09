print()

# Para leer un archivo se utiliza la función read() y existen tres métodos:

# Función read() permite leer todo el contenido del archivo:

with open("ejemplo.txt", "r") as file: # Esto abre el archivo ejemplo.txt modo lectura y lo renombra como "file"
    contenido = file.read()
    print(contenido) # Con with open ya no es necesario cerrar el archivo con close() ya que lo cierra automáticamente.

# Función readline() permite leer la primera línea del fichero:

with open("ejemplo.txt", "r") as file:
    linea = file.readline()
    print(linea)

# Función readlines() permite leer todas las líneas del archivo:

with open("ejemplo.txt", "r") as file:
    lineas = file.readlines()
    print(lineas)
print()