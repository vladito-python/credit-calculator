print()

# Conversión entre tipo de datos:


num = 100 # La variable "num" es tipo int y vamos a convertirla en texto.
texto = str(num)
print(type(texto)) # Imprime que el tipo de dato de la variable "texto" ahora es str.

num = 100 # La variable "num" es tipo int y vamos a convertirla en float.
decimal = float(num)
print(type(decimal)) # Imprime que el tipo de dato de la variable "decimal" ahora es float.

cadena = "100" # La variable "cadena" es tipo str y vamos a convertirla en número entero.
numero = int(cadena)
print(type(numero)) # Imprime que el tipo de dato de la variable "numero" ahora es int.

num = -3 # La variable "num" es tipo int y vamos a convertirla en booleano.
booleano = bool(num)
print(type(booleano)) # Imprime que el tipo de dato de la variable "booleano" ahora es bool.

lista = [1, 2, 3] # La variable "lista" es tipo list y vamos a convertirla en tupla.
tupla = tuple(lista)
print(type(tupla)) # Imprime que el tipo de dato de la variable "tupla" ahora es tuple.

print()