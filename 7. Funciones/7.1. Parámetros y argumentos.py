print()

# Las funciones permiten realizar tareas y reutilizar código para organizar mejor los programas.

def saludar(): # Esta función tiene nombre "saludar" sin parámetros dentro de (). 
    print("Hola! Bienvenido")

saludar() # Al llamar a la función por su nombre, esta imprime el saludo.
print()

# Los parámetros son variables que recibe la función dentro de () y los argumentos son los valores con los que se llama a la función:

def saludo(nombre): # saludo es el nombre que le damos a la función y nombre es el parámetro.
    print(f"Hola {nombre}! Bienvenido")

saludo("Ana") # Ana, Carlos, Luis y Python son los argumentos para llamar a la función. El argumento es el valor que le damos al parámetro.
saludo("Carlos")
saludo("Luis")
saludo("Python")
print()

# Los parámetros nos permiten reutilizar la función, es decir, la función sirve igual para diferentes argumentos.

# Cuando haya más de un parámetro, los argumentos se pasan en la posición de los parámetros, estos se conocen como argumentos posicionales:

def presentar(nombre, edad):
    """Esta función muestra en consola el nombre y edad de una persona""" # Dentro de las funciones es común usar los docstrings """ para documentar la función.
    print(f"Hola, me llamo {nombre} y tengo {edad} años")

presentar("Ana", 25) # Ana para nombre y 25 para edad.
print()

# Los argumentos se pueden establecer por defecto en los parámetros, estos se conocen como argumentos con valor por defecto:

def presentacion(nombre, edad, sexo = "Masculino"):
    print(f"Hola, me llamo {nombre}, tengo {edad} años y soy {sexo}")

presentacion("Luis", 25) # Luis para nombre y 25 para edad. El sexo ya está establecido por defecto.
presentacion("Ana", 25, "Femenino") # También se puede reescribir el valor por defecto.
print()

# Sin embargo, se puede llamar a la función cambiando la posición de los parámetros con sus argumentos, sin importar la posición en la que se definen en la función:

presentacion(edad = 25, sexo = "Femenino", nombre = "Ana")
print()