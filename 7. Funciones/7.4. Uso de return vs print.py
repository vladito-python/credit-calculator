print()

# Cuándo usar print y cuándo usar return en una función?

# Print y return funcionan correctamente en una función, la diferencia radica en cómo se usan:

# Si necesitas guardar uno o varios valores puros que devuelve una función para usarlos en otra parte del programa, usa return:

def calcular_total(cantidad:int, precio_unitario:float): # :int y :float son anotaciones que indican el tipo de dato que se espera recibir.
    resultado = (cantidad * precio_unitario)
    return resultado

total = calcular_total(3, 50) # El valor devuelto de la variable resultado se guarda en la variable total.
print(f"El total a pagar es: {total} pesos\n") # El valor ya asociado a una variable, se usa en este print.

# Si la función solo necesita mostrar o comunicar, usa print:

def saludo(nombre, hora):
    if hora >= 6 and hora < 12:
        print("Buenos dias,", nombre)
    elif hora >= 12 and hora < 20:
        print("Buenas tardes,", nombre)
    else:
        print("Buenas noches,", nombre)

saludo("Gerson", 15) # Aquí, sería innecesario llamar la función dentro de una variable, ya que no devuelve nada y si se hiciera, la consola mostraría el tipo None.
print()

# El uso de uno y otro dependerá también de cómo quieras estructurar y manejar tu programa:

def multiplicacion(x, y):
    resultado = (x * y)
    return resultado # La función está pensada para devolver un valor clave.

resultado = multiplicacion(7, 9) # Recuerda que las variables resultado, dentro y fuera de la función, son diferentes, incluso si llevan el mismo nombre. Para evitar confusiones, puedes usar nombres diferentes.
if resultado % 2 == 0:
    print(f"El resultado de la multiplicación es {resultado} y es número par\n")
else:
    print(f"El resultado de la multiplicación es {resultado} y es número impar\n")


def multiplicacion2(x, y):
    resultado = (x * y)
    if resultado % 2 == 0:
        print(f"El resultado de la multiplicación es {resultado} y es número par\n") # También se podría usar return en lugar de print, sin embargo, si sabes que el valor del return no lo usarás en otra parte, es innecesario.
    else:
        print(f"El resultado de la multiplicación es {resultado} y es número impar\n")

multiplicacion2(7, 9)