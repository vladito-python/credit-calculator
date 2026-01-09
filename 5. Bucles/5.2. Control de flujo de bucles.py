print("\n")

# Break: Detiene el flujo de ejecución del bucle:

contador = 0

while True:
    if contador >= 5:
        break
    print("Contador:", contador)
    contador += 2

print("\n")


while True: # while True es un bucle infinito.
    usuario = input("Ingresa el usuario correcto: ")
    if usuario == "admin":
        print("Bienvenido admin\n")
        break  # Aquí break detiene el bucle al ingresar el usuario como admin.


for num in range(1, 10): # Este rango recorre del 1 al 9, sin incluir el 10. # Comienza a recorrer desde el 1, procede a evaluar la condición, si no se cumple procede con el 2do print.
    if num == 5:
        print("Se encontró el 5, saliendo...\n")
        break # Al llegar al 5, el break detiene la iteración porque se cumplió la condición, procede con el 1er print y el bucle finaliza.
    print("Número:", num)


# Continue: Salta a la siguiente iteración del bucle:

for num in range(10): # for recorre desde el 0 hasta el 9. 
    if num == 5:
        continue # Cuando el número sea 5, el bucle comienza de nuevo a evaluar sin imprimir el 5.
    print(num)

print("\n")


contador = 0

while contador < 10:
    contador += 1
    if contador % 2 == 0: # Si el contador es par, el bucle comienza de nuevo a evaluar sin imprimir el número par.
        continue
    print("Número impar:", contador)

print("\n")