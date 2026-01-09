print()

# Try y except sirven para manejar errores sin que el programa se detenga cuando ocurre algo.
# En el try colocamos el código que puede generar un error.
# En el except se captura el error y se toma una acción.
# El finally se ejecuta haya o no haya errores.

def dividir(a, b):
    try:
        if a < 0 or b < 0:
            raise ValueError("No se permiten números negativos") # raise se usa para provocar un excepción personalizada.
        resultado = a / b
        return resultado
    except ZeroDivisionError: # Esta es una excepción especial de Python que ocurre cuando se intenta dividir entre cero.
        print("Error: No se puede dividir entre cero")
    except TypeError: # Esta es una excepción especial de Python que ocurre cuando se intenta realizar una operación con tipos de datos incompatibles.
        print("Error: Los valores deben ser numéricos")
    except ValueError as e: # Esta es una excepción especial de Python que ocurre cuando se intenta convertir un valor a un tipo de datos incompatibles.
        print(f"Error: {e}")
    except Exception as e: # Esta es una excepción especial de Python que captura la mayoría de los errores.
        print(f"Error inesperado: {e}")
    finally: # El finally se ejecuta haya o no haya errores.
        print("Fin del programa")

print(dividir(10, -4)) # Nota que si se ejecuta el raise, el except finaliza la función y nunca procede al return, por lo que la pantalla muestra None.


def acceso_votacion(años):
    if años < 18:
        return ("\nNo puedes votar. No cumples con la edad mínima") # Aquí se usa un return porque el valor devuelto se va a usar después en el main.
    else:
        return ("\nPuedes votar. Eres mayor de edad")

def main_1(): # Nota que en este ejercicio, las excepciones se declaran en una función principal.
    try:
        edad = input("\nIngresa tu edad: ")
        try:
            validar_flotante = float(edad) # Convertimos la edad a flotante.
            if not validar_flotante.is_integer(): # is_integer() verifica si el número es entero.
                raise TypeError("\nError: La edad debe ser un número entero") # Provocamos un TypeError personalizado cuando el usuario ingrese números decimales.
        except ValueError:
            raise TypeError("\nError: La edad introducida no es válida") # Provocamos un ValueError personalizado cuando el usuario ingrese caracteres no numéricos.
        validar_entero = int(validar_flotante) # Si las validaciones anteriores no generan errores, convertimos el número a entero.
        if validar_entero < 0:
            raise ValueError("\nError: La edad no puede ser negativa") # Provocamos un ValueError personalizado cuando el usuario ingrese números negativos.
        print(acceso_votacion(validar_entero))
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(e)

main_1()


def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def evaluar_imc(imc):
    if imc < 18.5:
        return "tienes bajo peso\n"
    elif imc < 24.9:
        return "tienes peso normal\n"
    elif imc < 29.9:
        return "tienes sobrepeso\n"
    else:
        return "tienes obesidad\n"

def programa_principal(): # Nota que en este ejercicio, las excepciones se declaran en una función principal.
    print("\nCALCULADORA DE IMC\n")
    nombre = input("Ingresa tu nombre: ") # Nota que la variable nombre está por fuera del try, ya que el usuario puede ingresar cualquier carácter para su nombre.
    try:
        peso = float(input("Ingresa tu peso en kg: "))
        altura = float(input("Ingresa tu altura en metros: "))
        if altura < 0 or peso < 0:
            raise ValueError("\nNo se admiten números negativos\n")
        imc = calcular_imc(peso, altura)
        print("\nRESULTADOS:\n")
        print("Tu IMC es:", imc)
        resultado_imc = evaluar_imc(imc)
        print(nombre, resultado_imc)
    except ValueError:
        print("\nError: Entrada inválida. Asegúrate de ingresar números (se permiten decimales) y no dejar campos vacíos.\n")
    except ZeroDivisionError:
        print("\nError: La altura no puede ser 0.\n")
    except Exception as e:
        print(e)

programa_principal()


# Para el siguiente ejercicio copia la siguiente frase:
# En el año 2023, compré 15 libros y 3 revistas para la colección de mi hermana.

def contar_caracteres(frase):
    vocales = "aeiouAEIOU"
    num_vocales = 0
    num_consonantes = 0
    num_digitos = 0
    num_espacios = 0
    for letra in frase:
        if letra.isalpha(): # isalpha() verifica si los caracteres son letras.
            if letra in vocales:
                num_vocales += 1
            else:
                num_consonantes += 1
        elif letra.isdigit(): # isdigit() verifica si los caracteres son dígitos.
            num_digitos += 1
        elif letra.isspace(): # isspace() verifica si existen espacios.
            num_espacios += 1
    return num_vocales, num_consonantes, num_digitos, num_espacios

def main_2():
    try:
        frase = input("Ingresa una frase: ").strip()
        if not frase:
            raise ValueError("Frase vacía")
        num_vocales, num_consonantes, num_digitos, num_espacios = contar_caracteres(frase)
        print("\nResultados:\n")
        print(f"Número de vocales: {num_vocales}")
        print(f"Numero de consonantes: {num_consonantes}")
        print(f"Número de dígitos: {num_digitos}")
        print(f"Número de espacios: {num_espacios}\n")
    except ValueError as e:
        print(f"\nError: {e}\n")
    except KeyboardInterrupt: # Esta es una excepción especial de Python que ocurre cuando el usuario cancela la operación.
        print("\nOperación cancelada por el usuario\n")
    except Exception as e:
        print(f"\nError inesperado: {e}\n")

main_2()


import json # Este módulo permite convertir datos entre python y json.

try:
    with open("respuestas.json", "r", encoding="utf-8") as archivo:
        respuestas = json.load(archivo)
except FileNotFoundError:
    print("Error: No se encontró el archivo 'respuestas.json'.")
    respuestas = {}
except json.JSONDecodeError:
    print("Error: El archivo 'respuestas.json' no tiene un formato válido.")
    respuestas = {}

def obtener_respuestas(mensaje):
    mensaje = mensaje.lower()
    for coincidencia in respuestas: # coincidencia recorre cada clave del diccionario respuestas.
        if coincidencia.lower() in mensaje:
            return respuestas[coincidencia] # Se usa esa clave para obtener su valor
    return respuestas["default"]

def main_3():
    print("\nHola! Soy el asistente de cursos Techmind.")
    print("Escribe 'salir' para terminar\n")
    while True:
        try:
            usuario = input("Tú: ")
            if usuario.lower() == "salir":
                print("Bot: Hasta luego!\n")
                break
            respuesta = obtener_respuestas(usuario)
            print("Bot:", respuesta)
        except KeyError:
            print("Bot: Lo siento, no tengo una respuesta para eso.")
        except KeyboardInterrupt:
            print("\nBot: Operación cancelada.")
            break

main_3()