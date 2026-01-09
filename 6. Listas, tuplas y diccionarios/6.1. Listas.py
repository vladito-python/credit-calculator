print("\n")

# Las listas son colecciones de datos ordenados:

frutas = ["Manzana", "Naranja", "Pera"] # Esta es una lista de cadenas de texto
print(frutas)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Esta es una lista de enteros
print(numeros)

combinados = ["hola", 1, True, 3.14] # Esta es una lista de diferentes tipos de datos
print(combinados)

vacia = [] # Esta es una lista vacía
print(vacia)

matriz = [[1, 2, 3], ["gato", "perro", "pez"], [True, False, True]] # Esta es una lista de listas
print(matriz)

# Para contar cuántos elementos hay en una lista se usa len():

print(len(numeros))

# Para imprimir elementos específicos según su índice o posición en la lista:

print(frutas[0]) # Manzana se posiciona en el índice 0 contando desde el inicio. El primer elemento de una lista siempre se cuenta como el índice 0
print(numeros[1]) # 2 se posiciona en el índice 1 contando desde el inicio.
print(combinados[-1]) # 3.14 se posiciona en el índice -1 contando desde el final
print(matriz[1][0]) # gato se posiciona en la lista 1 con índice 0. Aquí primero se accede al indice de la lista y luego al indice del elemento de esa lista
print(numeros[1:4]) # Imprime los elementos 2, 3 y 4 desde el índice 1 hasta el índice 4 (el índice 4 no se incluye)
print(numeros[:3]) # Imprime los elementos 1, 2 y 3 desde el índice 0 hasta el índice 3 (el índice 3 no se incluye)
print(numeros[3:]) # Imprime los elementos 4, 5, 6, 7, 8, 9 y 10 desde el índice 3 hasta el final
print(numeros[:]) # Imprime todos los elementos desde el índice 0 hasta el final
print(numeros[::2]) # Imprime los elementos 1, 3, 5, 7 y 9 desde el índice 0 hasta el final saltando 2 cada vez
print(numeros[1::3]) # Imprime los elementos 2, 5 y 8 desde el índice 1 hasta el final saltando 3 cada vez
print(numeros[1:5:2]) # Imprime los elementos 2 y 4 desde el índice 1 hasta el índice 5 saltando 2 cada vez

