print()

# Formateo de cadenas y concatenación:

nombre = "Juan" # El tipo de datos de la variable "nombre" es str o cadena de texto.
edad = 24 # El tipo de datos de la variable "edad" es int.
print("Hola " + nombre) # El signo + únicamente se usa para concatenar str o cadena de texto.

# Para concatenar str con int hay diferentes formas:

# 1. Convertir int en str:

saludo = "Hola, mi nombre es " + nombre + " y tengo " + str(edad) + " años."
print(saludo)

# 2. Usar el método .format al final de la cadena:

saludo = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print(saludo)

# 3. El más versátil es el método f string, colocando la f delante de la cadena:

saludo = f"Hola, mi nombre es {nombre} y tengo {edad} años."
print(saludo)

print()
