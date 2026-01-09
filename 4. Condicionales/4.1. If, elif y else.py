# Los condicionales permiten tomar decisiones con base a condiciones específicas:

x = 15

if x > 15: # El condicional if coloca una primera condición
    print("\nx es mayor que 15\n")
elif x > 5: # El condicional elif coloca una segunda condición
    print("\nx es mayor que 5 pero menor que 15\n")
else: # El condicional else se usa si todas las demás condiciones no se cumplen
    print("\nx es menor o igual que 5\n")


nota = 60

if nota >= 90:
    print("Excelente\n")
elif nota >= 70:
    print("Aprobado\n")
else:
    print("Reprobado\n")


edad = 20
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puedes conducir\n")
else:
    print("No puedes conducir\n")


usuario = "admin"
clave = "6742"

if usuario == "admin" or clave == "1234":
    print("Acceso permitido\n")
else:
    print("Acceso no permitido\n")


llueve = True

if not llueve:
    print("Sale sin paraguas\n")
else:
    print("Lleva paraguas\n")


a = -5
b = -12
resta = (a - b)

if resta > 0 and (resta % 2) == 0:
    print(f"{resta} es número positivo y par\n")
elif resta > 0 and (resta % 2) != 0: 
    print(f"{resta} es número positivo e impar\n")
elif resta < 0 and (resta % 2) == 0:
    print(f"{resta} es número negativo y par\n")
else:
    print(f"{resta} es número negativo e impar\n")