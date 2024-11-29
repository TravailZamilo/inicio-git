#Desarrolla un programa que reciba 3 números e imprima el número mayor sólo utiliza condicionales


numero1 = int(input("Dame 3 números y te diré cual es mayor "))
print(f"Seleccionaste el número: {numero1}")
    
numero2 = int(input(f"ingresa el segundo número: "))
print(f"Seleccionaste el número: {numero2}")
    
numero3 = int(input(f"ingresa el tercer número: "))
print(f"Seleccionaste el número: {numero3}")
  
if numero1 > numero2 and numero1 > numero3:
    print(f"El número mayor es: {numero1}")

elif numero2 > numero1 and numero2 > numero3:
    print(f"El número mayor es: {numero2}")
    
else:
    print(f"El número mayor es: {numero3}")
    
print(f"Gracias por participar")

