print("\n")

# Las listas son mutables, es decir, sus valores pueden cambiar, lo que las hace flexibles, para ello hay diferentes metodos:

frutas = ["Manzana", "Banana", "Mango", "Uva"]

# Para modificar un elemento de una lista según su índice o posición en la lista:

frutas[0] = "Fresa" # Reemplaza manzana por fresa
print(frutas)

# Para añadir un elemento al final de una lista se usa .append():

frutas.append("Kiwi")
print(frutas)

# Para añadir un elemento a una lista en una posición específica se usa .insert():

frutas.insert(1, "Uva") # Inserta uva en el índice 1
print(frutas)

# Para añadir varios elementos al final de una lista se usa .extend():

frutas.extend(["Pera", "Piña", "Mango"])
print(frutas)

# Para eliminar la primera aparición de un elemento se usa .remove():

frutas.remove("Uva") # Nota que no elimina todas las uvas que puedan existir en la lista
print(frutas)

# Para eliminar el último elemento de la lista se usa .pop():

frutas.pop()
print(frutas)

# Para eliminar un elemento de una lista según su índice o posición en la lista se usa .pop():

frutas.pop(1) # Elimina el elemento en el índice 1
print(frutas)

# Para eliminar todos los elementos de una lista se usa .clear():

frutas.clear()
print(frutas)


numeros = [3, 20, 11, 100, 75, 15, 3]

# Para ordenar los elementos de una lista se usa .sort():

numeros.sort()
print(numeros)

# Para ordernar los elementos de una lista creando una nueva lista se usa sorted():

numeros_ordenados = sorted(numeros)
print(numeros_ordenados)

# Para contar el número de veces que aparece un elemento en una lista se usa .count():

numeros.count(3)
print(numeros.count(3))

print ("\n")