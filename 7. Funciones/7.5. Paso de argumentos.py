print()

# Hasta ahora, hemos dado argumentos a las funciones directamente al llamar la función, sin embargo, los argumentos pueden venir de variables, de returns de otras funciones o como parámetros de otras funciones.

def calcular_area(altura, base):
    resultado = (altura * base)
    return resultado

a = float(input("Digita la altura: ")) # a y b son variables globales que reciben un valor ingresado por el usuario.
b = float(input("Digita la base: "))

area = calcular_area(a, b) # a y b ahora son los argumentos de la función calcular_area: a para altura y b para base.
print(f"El área es: {area}\n")

# La función nunca sabe de dónde viene el argumento, solo recibe el valor final.

def multiplicacion(x, y):
    mult = (x * y)
    return mult

def mostrar_resultados(resultado):
    resultado = resultado
    if resultado % 2 == 0:
        print(f"El resultado de la multiplicación es {resultado} y es número par\n")
    else:
        print(f"El resultado de la multiplicación es {resultado} y es número impar\n")

mostrar_resultados(multiplicacion(2, 2)) # El argumento de la función mostrar_resultados es el valor devuelto por la función multiplicacion.
mostrar_resultados(multiplicacion(10, 6))


def titulo():
    print("Sistema de Evaluación de Estudiantes\n")

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

def evaluar_estudiante(nombre, promedio):
    if promedio >= 70 and promedio <= 100:
        return (f"{nombre} aprobó con un promedio de {promedio:0.2f}\n")
    elif promedio < 70 and promedio >= 0:
        return (f"{nombre} reprobó con un promedio de {promedio:0.2f}\n") # Promedio:0.2f significa que el valor tiene 2 decimales.
    else:
        return ("Error: notas inválidas\n")

def resultados(nombre, n1, n2, n3):
    promedio_estudiante = calcular_promedio(n1, n2, n3) # los argumentos de la función calcular_promedio son ahora los parámetros de la función resultados.
    resultado = evaluar_estudiante(nombre, promedio_estudiante) # El segundo argumento de la función evaluar_estudiante es la variable local promedio_estudiante.
    return resultado

titulo()
print(resultados("Gerson", 85, 70, 90))
print(resultados("Ana", 50, 50, 90))
print(resultados("Juan", 60, 60, 60))


def mostrar_menu():
    print("----Menú de Opciones----\n")
    print("1. Sumar dos números")
    print("2. Saludar")
    print("3. Salir")

def sumar_numeros(a, b):
    suma = (a + b)
    return suma

def saludar(nombre):
    nombre = nombre # Nota que el editor hace distinción tipográfica y de color entre el parámetro y la variable local.
    return nombre

while True:
    mostrar_menu()
    opcion = int(input("\nEscoge una opción: "))
    if opcion == 3:
        print("\nHasta luego...\n")
        break
    elif opcion == 1:
        numero1 = int(input("\nIngresa el primer número: "))
        numero2 = int(input("Ingresa el segundo número: "))
        resultado = sumar_numeros(numero1, numero2) # las variables globales numero1 y numero2 son argumentos de la función sumar_numeros.
        print(f"La suma es {resultado}\n")
    elif opcion == 2:
        pregunta_nombre = input("\nCómo te llamas?: ")
        nombre = saludar(pregunta_nombre) # la variable global pregunta_nombre es argumento de la función saludar. Recuerda también que la variable global nombre no es la misma que la local nombre de la función saludar.
        print(f"Hola {nombre}!\n")
    else:
        print("\nOpción no válida. Intenta de Nuevo\n")