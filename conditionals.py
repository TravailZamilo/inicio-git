respuestaUsuario = input("¿Te gustaría comprar sellos, comprar un sobre o hacer una copia? (Escribe sellos, sobre o copia) ")

if respuestaUsuario in ("sellos", "sobre", "copia"):  
    print(f"Seleccionaste la opción: {respuestaUsuario}.")  
    if respuestaUsuario == "sellos":
        print(f"Tenemos muchos tipos de {respuestaUsuario} para elegir.")
    elif respuestaUsuario == "sobre":
        print(f"Tenemos muchos tipos de {respuestaUsuario} para elegir.")
    elif respuestaUsuario == "copia":
        copias = input("¿Cuántas copias te gustaría? (Escribe un número) ")
        print(f"Aquí tienes {copias} copias.")
else:
    print(f"Gracias, por favor vuelve pronto.")