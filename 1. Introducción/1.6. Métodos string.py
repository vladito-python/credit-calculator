print()

# Los métodos string son acciones que se pueden realizar sobre los strings:

nombre = "---gerson g.s---"

print(nombre.upper()) # Convierte todos los textos en mayúsculas. No tiene argumentos dentro de los paréntesis.
print(nombre.lower()) # Convierte todos los textos en minúsculas. No tiene argumentos dentro de los paréntesis.
print(nombre.title()) # Coloca la primera letra de cada palabra en mayúsculas. No tiene argumentos dentro de los paréntesis.
print(nombre.capitalize()) # Coloca solo la primera letra en mayúscula. Si el primer caracter es un espacio, lo capitaliza y el resto lo deja igual. No tiene argumentos dentro de los paréntesis.
print(nombre.count("o")) # Cuenta las veces que aparece una letra o palabra dentro del texto o cadena.
print(nombre.find("gerson")) # Indica en qué posición inicia una letra o texto contando desde 0 incluyendo los espacios.
print(nombre.replace("g.s", "galindres saa")) # Reemplaza parte del texto, tal cual aparece, por otro.
print(nombre.strip("-")) # Elimina los espacios y otros caracteres del inicio y el final del string, no del medio.

# Se pueden combinar varios métodos:

nombre = nombre.replace("g.s", "galindres saa")
nombre = nombre.title()
nombre = nombre.strip("-")
print(nombre) # El orden de ejecución importa y se imprimirá el último valor de la variable (tipado dinámico).

print()
