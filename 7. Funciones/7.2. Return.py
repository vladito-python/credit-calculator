print()

# Funciones con Return: Permite devolver un valor para que otras partes del programa lo reutilicen.

def sumar(a, b):
    return (a + b)

print(sumar(10, 5)) # Al llamar la función, return devolverá el valor de la suma de a y b y finaliza. Para poder mostrarlo en pantalla es necesario usar print().

resultado = sumar(10, 5) # También puedes guardar el valor en una variable y luego mostrarlo en pantalla.
print(resultado)
print()

def saludar(nombre):
    return nombre # Aquí se devuelve simplemente el valor de nombre

saludo = saludar("Gerson") # El valor de nombre se guarda en la variable saludo, preferiblemente.
print(f"Hola {saludo}!") # Ese valor asociado a la variable saludo es usado ahora en este print.
print()

# Una función puede devolver más de un valor de return pero el valor se devolverá en orden de declaración del return:

def datos_persona(nombre, edad, altura):
    return edad, altura, nombre

edad_persona, altura_persona, nombre_persona = datos_persona("Gerson", 22, 1.75) # Los argumentos se pasan en la posición de los parámetros.
print("Edad:", edad_persona) # El return devolverá, en orden de declaración, la edad, la altura y por último el nombre.
print("Altura:", altura_persona)
print("Nombre:", nombre_persona)
print()

# Se puede acceder a cada valor devuelto por el return usando la notación de índice:

def calcular_areas(a, b):
    return (a + b), (a * b) / 2

resultado = calcular_areas(10, 5)
print("El área del rectángulo es:", resultado[0]) # resultado[0] es el primer valor devuelto por el return.
print("El área del triángulo es:", resultado[1]) # resultado[1] es el segundo valor devuelto por el return.
print()

# Cuando hay más de un return, solo uno se ejecutará por llamada, el resto de código se ignora:

def es_mayor_de_edad(edad):
    if edad >= 18: # Si esta condición se cumple, se devuelve el return con valor True y finaliza la función.
        return True 
    return False # Si la condición no se cumple, se devuelve el return con valor False y finaliza la función.

print("Es mayor de edad:", es_mayor_de_edad(18)) # Recuerda que puedes mostrar el valor del return con print o en una variable y luego mostrarla en pantalla.
print()


def evaluar_numero(n):
    if n > 0:
        return "Positivo"
    elif n < 0:
        return "Negativo"
    return "Cero"

print("El número es:", evaluar_numero(10))
print()
