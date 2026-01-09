print("\n")

# Operadores lógicos:

a = 10
b = 3
c = 10
print("a es mayor a b y a es igual a c?", (a > b) and (a == c)) # and verifica que se cumplan las dos condiciones para que el resultado sea verdadero (true), de lo contrario será falso (false).
print("a es mayor a b y a es menor a c?", (a > b) and (a < c))
print("a es mayor que b ó a es menor que c?", (a > b) or (a < c)) # or verifica que se cumpla al menos una de las condiciones para que el resultado sea verdadero (true).
print("Negación de a > b:", not (a > b)) # not invierte el valor de la condición. Imprime false ya que invierte el valor lógico: a sí es mayor que b (true).

print("\n")