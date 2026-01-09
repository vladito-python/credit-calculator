def mostrar_opciones():
    print("\n1 = Suma\n2 = Resta\n3 = Multiplicación\n4 = División\n5 = Salir")

def sumar(*numeros):
    suma = 0
    for n in numeros:
        suma += n
    return suma

def restar(*numeros):
    resta = numeros[0]
    for n in numeros[1:]:
        resta -= n
    return resta

def multiplicar(*numeros):
    multiplicacion = 1
    for n in numeros:
        multiplicacion *= n
    return multiplicacion

def dividir(*numeros):
    division = numeros[0] # Aquí division es igual al número con índice 0.
    for n in numeros[1:]: # Aquí itera desde el número con índice 1 hasta el final.
        division /= n
    return division

def programa_principal():
    print("\nBienvenido a la Calculadora de Python")
    while True:
        mostrar_opciones()
        try:
            opcion = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("\nError: Por favor, ingrese un número entero válido para la opción.")
            continue
        if opcion == 5:
            print("\n¡Hasta luego! Gracias por usar la Calculadora\n")
            break
        if opcion in range(1, 5):
            try:
                entrada = input("\nIngrese los números separados por espacio: ").split()
                if not entrada:
                    print("\nError: No se ingresaron números.")
                    continue
                numeros = list(map(int, entrada))
            except ValueError:
                print("\nError: Por favor, ingrese solo números enteros separados por espacio.")
                continue
            try:
                if opcion == 1:
                    suma = sumar(*numeros)
                    print("\nEl resultado es:", suma)
                elif opcion == 2:
                    resta = restar(*numeros)
                    print("\nEl resultado es:", resta)
                elif opcion == 3:
                    multiplicacion = multiplicar(*numeros)
                    print("\nEl resultado es:", multiplicacion)
                elif opcion == 4:
                    division = dividir(*numeros)
                    print("\nEl resultado es:", division)
            except ZeroDivisionError:
                print("\nError: No se puede dividir por cero.")
            except IndexError:
                print("\nError: Se necesitan al menos dos números para realizar la operación.")
            except Exception as e:
                print(f"\nOcurrió un error inesperado: {e}")
        else:
            print("\nOpción inválida. Intente de nuevo.\n")
        
        print("\n¿Desea realizar otra operación?")

programa_principal()