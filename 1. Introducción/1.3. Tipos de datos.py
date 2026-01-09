print()

# Principales tipos de datos:

# Datos básicos:

# Dato tipo int = Número entero:

x = 10
print(type(x)) # El comando type muestra el tipo de datos de la variable.

# Dato tipo float = Número decimal:

y = 3.1416
print(type(y))

# Dato tipo str = String o texto o cadena de texto. Los textos o str siempre van dentro de ""

z = "Hola Python"
print(type(z))

# Dato tipo bool = Booleano True y False:

es_mayor = True
print(type(es_mayor))

es_menor = False
print(type(es_menor))

# Los booleanos se usan también en operadores lógicos:

print(5 > 2) # Bool = Dato booleano True.
print(10 < 4) # Bool = Dato booleano False.

# Datos compuestos:

# Dato tipo list = Listas o colecciones de datos ordenados y mutables (modificables) y van entre []:

mixta = [10, "Python", True]
print(type(mixta))

# Dato tipo tuple = Tuplas o colecciones de datos ordenados e inmutables (no se modifican después de crearlos) y van entre ():

colores = ("Rojo", "Verde" ,"Azul")
print(type(colores)) 

# Dato tipo set = Conjuntos desordenados que no permiten valores duplicados y van entre {}:

conjunto = {1, 2, 2, 4, 6, 6}
print(type(conjunto))
print(conjunto) # Imprime los números y elimina los duplicados.

# Dato tipo dict = Diccionarios o estructuras que almacenan datos en pares (clave, valor):

persona = {
    "Nombre": "Juan",
    "Edad": 24,
    "Activo": True
}
print(type(persona))

# Otro tipo de datos:

# Dato tipo complex = Es un número complejo:

ecuacion = 2 + 3j
print(type(ecuacion))

# Dato tipo None = Nulo o vacío:

nulo = None
print(type(nulo))

# Dato tipo range = Rango o secuencia de números:

rango = range(6) # Genera una secuencia de números del 0 al 5.
print(type(rango))
print(rango)

rango = range(1, 6) # Genera una secuencia de números del 1 al 5.
print(rango)

rango = range(1, 6, 2) # Genera una secuencia de números del 1 al 5 saltando 2 en 2.
print(rango)

rango = range(-5, 0) # Genera una secuencia de números del -5 al -1.
print(rango)

print()