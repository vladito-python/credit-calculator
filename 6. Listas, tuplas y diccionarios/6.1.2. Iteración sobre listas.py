print("\n")

# Para iterar sobre listas se usa el bucle for:

frutas = ["manzana", "pera", "cereza"]

for fruta in frutas:  # For recorre cada elemento de la lista frutas con nombre fruta.
    print("Me gusta la", fruta) # Es decir, for recorre a fruta = Manzana, fruta = Pera, fruta = Cereza, etc. 

print("\n")


precios = [100, 200, 150]
total = 0

for precio in precios: # For recorre cada precio en la lista. Precio = 100, precio = 200, precio = 150
    total += precio # Esto significa total = total + precio, inicia con total = 0 + 100, luego total = 100 + 200, etc.
print(f"El total es: {total}")

print("\n")


colores = ["rojo", "verde", "azul"]

for posicion, color in enumerate(colores): # Cuando se usa enumerate, la primera posición es el índice y el segundo es el valor.
    print(f"La posición {posicion} corresponde al color {color}")

print("\n")


letras = ["a", "b", "c"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros: # Anidado de bucles. Este for se ejecuta por cada iteración del bucle exterior.
        print(letra, numero)

print("\n")


animales = ["perro", "lobo", "elefante", "gato", "pez"]

for posicion, animal in enumerate(animales):
    if animal == "gato":
        print("Encontré al gato, está en el índice", posicion)
        break
    print(animal)

print("\n")
