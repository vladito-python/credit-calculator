print()

# Las funciones permiten establecer variables dentro de ellas, estas variables se conocen como variables locales y solo se usan dentro de la función.
# Las variables globales son aquellas que se establecen fuera de una función y no guardan ninguna relación con las variables locales de la función.

def restar(a, b):
    resta = (a - b) # Se establece una variable local llamada resta dentro de la función.
    return resta # Return siempre devolverá el valor (a - b) de la variable resta, no la variable en sí.

resta = restar(10, 5) # Esta variable, también llamada resta, es una variable global, está por fuera de la función y aunque puede llamarse como la variable local, son dos variables diferentes.  
print("La resta es:", resta)
print()

# No es obligatorio usar variables locales pero es una buena práctica para mejorar la legibilidad del código:

def calcular_areas(a, b):
    rectangulo = (a * b)
    triangulo = (a * b) / 2
    return rectangulo, triangulo # Return devuelve el valor (a * b) de la variable rectangulo y el valor (a * b) / 2 de la variable triangulo.

area_rectangulo, area_triangulo = calcular_areas(10, 5) #  area_rectangulo para rectangulo y area_triangulo para triangulo, tal como el orden del return lo indica.
print("El área del rectángulo es:", area_rectangulo)
print("El área del triángulo es:", area_triangulo)
print()


def sumar(*args): # *args permite una cantidad variable de argumentos como tupla.
    suma = 0
    for n in args:
        suma += n
    return suma

suma = sumar(1, 2, 3, 4, 5)
print("La suma es:", suma)
print()