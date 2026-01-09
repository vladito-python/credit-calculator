print()

# Para abrir un archivo se utiliza la función open(), la cual requiere al menos de dos argumentos: el nombre o ruta del archivo y el modo de apertura.
# Existen tres modos de abrir un archivo:

# Modo lectura "r" permite leer el contenido del archivo:

archivo = open(r"C:\Users\GERSON G.S\OneDrive\Desktop\curso python\ejemplo.txt", "r") # Se puede usar la ruta completa del archivo o colocando el nombre del archivo:
archivo = open("ejemplo.txt", "r") # De esta manera, el archivo debe estar en la misma carpeta que el archivo .py
archivo.close() # Esto cierra el archivo después de usarlo

# Modo escritura "w" permite escribir en el archivo, si el archivo no existe, se creará:

archivo = open("ejemplo.txt", "w")
archivo.close()

# Agregar contenido "a" permite agregar contenido al final del archivo sin sobreescribirlo:

archivo = open("ejemplo.txt", "a")
archivo.close()


