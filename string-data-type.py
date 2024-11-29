miCadena = "Este es un string."
print(f"miCadena")  # Aquí no se interpreta la variable, imprime literalmente "miCadena".
print(type(miCadena))  # Muestra el tipo de dato de la variable.
print(miCadena + " es del tipo de dato " + str(type(miCadena)))  # Combina texto y el tipo de dato.

primeraCadena = "agua"
segundaCadena = "cascada"
terceraCadena = primeraCadena + " " + segundaCadena  # Concatenar las dos cadenas
print(terceraCadena)  # Imprimir el resultado