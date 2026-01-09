print()

# La función input() solicita al usuario que ingrese información de manera interactiva:

pregunta = "Cómo te llamas? "
nombre = input(pregunta) # Input solicita que el usuario ingrese su nombre.

# La función input() también puede estar dentro de una variable:

nombre = input("\nCómo te llamas? ") # Antes de imprimir el saludo, input solicitará el nombre del usuario.
print("Hola " +nombre+ "! Bienvenido a Python\n") # Independientemente de lo que escriba el usuario, input devuelve un valor str por defecto, por eso se usa el signo + para concatenar la variable nombre.

# Se pueden obtener múltiples entradas de información usando la función split(), siempre que sean de tipo str:

pais, ciudad = input("En qué país y ciudad vives? ").split() # split() divide el string en una lista de subcadenas, separadas por espacios por defecto.
print(f"Vives en {pais}, {ciudad}\n")

# Para trabajar con un tipo de datos diferente a str, que está por defecto, se usa la conversión de tipo de datos:

edad = int(input("Ingresa tu edad: ")) # int convertirá el valor str ingresado por el usuario a un número entero, siempre que se pueda, de lo contrario lanzará error al intentar por ejemplo, convertir "hola" en entero.
print("En 5 años tu edad será:", edad + 5, "años\n")

establo1 = float(input("Ingresa litros de leche establo 1: ")) # float permitirá trabajar con números decimales.
establo2 = float(input("Ingresa litros de leche establo 2: "))
print("El total de litros de leche hoy son:", establo1 + establo2, "litros\n")