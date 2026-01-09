print("\n")

# Los bucles permiten repetir un bloque de código varias veces. Existen dos tipos principales:

# Bucle for: Se usa para repetir el código mientras itera sobre un iterable y va acompañado del comando in:

for i in range(5): # En cada iteración de la variable i, for recorre el rango de números desde el 0 hasta 4, sin incluir el 5.
    print("Número:", i) # Es decir, for recorre a i = 0, i = 1, i = 2, etc.

print("\n")


for letra in "Python": # For recorre cada letra de la palabra python en la variable letra.
    print(letra) # Es decir, for recorre a letra = P, letra = y, letra = t, etc.

print("\n")

# Bucle while: Se usa para repetir el código mientras una condición sea verdadera, si ya no se cumple, se detiene.

contador = 0

while contador <= 5: 
    print("Contador:", contador)
    contador += 2 # Una vez evalúe que la condición se cumpla, prosigue con el print y luego de esto, suma 2 al contador y comienza de nuevo el bucle.
    # Aquí += 2 significa contador = contador + 2, esto es lo que hará que la condición posteriormente ya no se cumpla, de lo contrario será un bucle infinito. 
print("\n")


usuario = ""

while usuario != "admin": # Mientras el usuario ingrese un nombre distinto a "admin", la consola seguirá solicitando usuario correcto dado en el input.
    usuario = input("Ingresa el usuario correcto: ") 
print("Bienvenido admin\n") # Si el usuario ingresa "admin", la condición ya no se cumple y procede a imprimir el saludo.


x = 0
i = 0

while x != 7:
    x = int(input("Adivina el número del 1 al 10: "))
    i += 1
    print(f"Intento número {i}")
print("Ese es el número!\n")