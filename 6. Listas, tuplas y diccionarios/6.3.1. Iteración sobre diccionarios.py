print("\n")

# Para iterar sobre diccionarios se utiliza el bucle for:

personas = {"nombre": "Gerson",
            "edad": 20, 
            "ciudad": "Santiago"}

for clave, valor in personas.items():  # For recorre cada clave y valor del diccionario personas.
    print(valor)

print("\n")


inventario = {"manzana": 3,
                "naranjas": 5,
                "bananos": 2}

for fruta, cantidad in inventario.items():
    print(f"{fruta}: {cantidad}")

print("\n")