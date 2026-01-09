import calendar as cl

print("\nBienvenido a mi Calendario Python")

def calendario(): # En este ejercicio, un poco más complejo, con el fin de comprender mejor el código he decidido usar la función sin parámetros
    while True:
        try:
            año = int(input("\nQué año quieres revisar?: "))
            if año == 0:
                print("\nIngresa un año diferente de 0")
                continue
            mes = int(input("Qué mes quieres que muestre?: "))
            if mes not in range(1, 13):
                print("\nError: El mes debe ser un número del 1 al 12")
                continue
            print(f"\nAquí tienes el calendario del mes {mes} del año {año}:\n")
            resultado = cl.month(año, mes)
            return resultado
        except ValueError:
            print("\nError: Número de año o mes inválido")

print(calendario())

while True:
    respuesta_usuario = ""
    try:
        respuesta_usuario = input("Quieres que revise otro calendario? Escribe 'Si' o 'No': ")
        if respuesta_usuario.lower() == "no":
            print("\nHasta luego! Gracias por usar mi Calendario\n")
            break
        elif respuesta_usuario.lower() == "si":
            print(calendario())
        else:
            print("\nError: Opción no válida\n")
    except ValueError:
        print("\nError: Opción no válida\n")