import random
import string

# Función para validar el formato del código
def validar_codigo(codigo):
    # El patrón esperado
    if len(codigo) != 11:
        return False
    if not codigo[:3].isalpha() or not codigo[:3].isupper():  # Tres letras al inicio
        return False
    if not codigo[3].isdigit():  # Un número en la posición 4
        return False
    if not codigo[4].isalpha() or not codigo[4].isupper():  # Una letra en la posición 5
        return False
    if not codigo[5:10].isdigit():  # Cinco números consecutivos
        return False
    if not codigo[10].isalpha() or not codigo[10].isupper():  # Una letra al final
        return False
    return True

# Función para generar códigos aleatorios válidos
def generar_codigos_reducidos(cantidad=10, prefijos=["RKA", "DLQ", "LIN"]):
    codigos = []
    while len(codigos) < cantidad:
        # Seleccionar un prefijo permitido
        parte1 = random.choice(prefijos)
        parte2 = f"{random.randint(0, 9)}{random.choice(string.ascii_uppercase)}"  # Un número y una letra
        parte3 = ''.join(random.choices(string.digits, k=5))  # Cinco números consecutivos
        parte4 = random.choice(string.ascii_uppercase)  # Una letra al final
        codigo = f"{parte1}{parte2}{parte3}{parte4}"
        
        # Validar antes de agregar
        if validar_codigo(codigo):
            codigos.append(codigo)
    return codigos

# Generar 10 códigos reducidos
codigos_reducidos = generar_codigos_reducidos()
for codigo in codigos_reducidos:
    print(codigo)