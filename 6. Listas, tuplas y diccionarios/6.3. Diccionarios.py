print("\n")

# Los diccionarios son una colección de datos que se almacenan en pares de clave y valor.

personas = {"nombre": "Gerson",  # Las claves identifican cada valor dentro del diccionario. Nombre es la clave y Gerson es el valor, etc.
            "edad": 32,
            "pais": "Colombia"}
print(personas)

print("\n")

# Para acceder a un valor dentro del diccionario, se utiliza la clave entre []:

print(personas["nombre"])

print("\n")

# Para modificar un valor dentro del diccionario, se utiliza la clave y se asigna el nuevo valor:

personas["edad"] = 21
print(personas)

print("\n")

# Para agregar un valor dentro del diccionario, se utiliza una nueva clave y se asigna su valor:

personas["profesion"] = "Programador"
print(personas)

print("\n")

# Para eliminar un valor dentro del diccionario, se utiliza la clave y la función del:

del personas["edad"]
print(personas)

print("\n")

# Para obtener las claves de un diccionario, se utiliza el método keys():

print(personas.keys())

print("\n")

# Para obtener los valores de un diccionario, se utiliza el método values():

print(personas.values())

print("\n")