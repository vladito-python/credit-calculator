print("\n")

# Las list comprehension son una forma rápida y compacta de crear una lista sin usar un for con append:

numeros = []

for i in range(1, 6): # Esta es la forma tradicional
    numeros.append(i)
print(numeros)

numeros2 = [i for i in range(1, 6)] # Esta es la forma más compacta en una sola línea
print(numeros2)


# Otros ejemplos:

cuadrados = [(i ** 2) for i in range(1, 10)]
print(cuadrados)


pares = [n for n in range(1, 10) if (n % 2) == 0]
print(pares)


animales = ["perro", "gato", "pez"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

print("\n")