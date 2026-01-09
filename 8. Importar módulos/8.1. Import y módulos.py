print()

# Import trae código de otros módulos o librerías externas para usar sus funciones:

import math # Import importa o trae el módulo matemática para usar sus funciones.

raiz_cuadrada = math.sqrt(16) # El módulo math usa la función raíz cuadrada sqrt.
print(raiz_cuadrada)
print()

numero_entero = math.ceil(4.3) # La función ceil redondea un número hacia arriba.
print(numero_entero)
print()

# También se puede usar funciones específicas de un módulo usando from:

from math import sqrt

raiz_cuadrada = sqrt(64) # Aquí se usa la función sqrt directamente.
print(raiz_cuadrada)
print()


from random import choice  # El módulo random con la función choice (solo para listas), elige un elemento aleatorio de una lista:

frutas = ["Manzana", "Banano", "Mora"]

fruta = choice(frutas)
print(fruta)
print()

# Los módulos pueden acortar su nombre con un alias usando as:

import random as rm

numeros = [1, 2, 3, 4, 5, 6]

numero = rm.choice(numeros)
print(numero)
print()


def sorteo(lista):
    ganador = rm.choice(lista)
    return ganador

def programa_principal():
    participantes = []
    print("Bienvenido al Generador de Sorteos\n")
    while True:
        nombre = input("Ingresa el nombre del participante: ")
        if nombre.lower() == "salir":
            print("\nEl sorteo ha terminado")
            break
        participantes.append(nombre)
    if len(participantes) < 2:
        print("\nNo hubo ganador. Se necesitan al menos 2 participantes para el sorteo\n")
    else:
        ganador = sorteo(participantes)
        print(f"\nEl ganador del sorteo es: {ganador}!\n")

programa_principal()


from random import randint

def calcular_calorias_quemadas(tiempo, peso):
    calorias = (tiempo * 3.5 * peso) / 200
    return calorias

def calorias_consumidas(min, max):
    calorias = randint(min, max) # La función randint del módulo random genera un número entero aleatorio dentro de un rango.
    return calorias

def comidas(lista):
    comida = rm.choice(lista)
    return comida

def programa_principal2():
    print("Calculadora de Calorías\n")
    nombre = input("Ingresa tu nombre: ")
    peso_kg = int(input("Ingresa tu peso en kg: "))
    minutos = int(input("Ingresa el tiempo de ejercicio en minutos: "))
    lista_comidas = ["pizza", "ensalada", "hamburguesa", "pollo", "fruta"]
    calorias_quemadas = calcular_calorias_quemadas(minutos, peso_kg)
    comida = comidas(lista_comidas)
    calorias = calorias_consumidas(50, 400)
    print(f"\n{nombre}, comiste {comida} con {calorias} Kcal.\n")
    print(f"Calorías quemadas corriendo {minutos} minutos: {calorias_quemadas} Kcal.\n")
    balance = math.ceil(calorias - calorias_quemadas)
    if balance > 0:
        print(f"Has consumido {balance} calorías más de las que quemaste.\n")
    else:
        print(f"Buen trabajo! Has quemado {abs(balance)} calorías más de las que comiste.\n") # abs devuelve el valor absoluto de un número.

programa_principal2()


def adivinar_numero(inicio, final):
    numero = rm.randint(inicio, final)
    return numero

def programa_principal3():
    min = 1
    max = 100
    num_secreto = adivinar_numero(min, max)
    intentos = 0
    print("Bienvenido al Juego de Adivinar el Número\n")
    while True:
        num_usuario = int(input(f"Adivina el número del {min} al {max}: "))
        intentos += 1
        if num_usuario == num_secreto:
            print("\nAdivinaste el número!\n")
            print(f"Intentos: {intentos}\n")
            break
        elif num_usuario > num_secreto:
            print("\nEl número es menor\n")
        else:
            print("\nEl número es mayor\n")

programa_principal3()
