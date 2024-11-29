# Guardar la secuencia de insulina sin procesar
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"


# Almacenamos cada secuencia de elementos

lsInsulin = "malwmrllpllallalwgpdpaaa"

bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"

aInsulin = "giveqcctsicslyqlenycn"

cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

# guardamos las agrupaciones más pequeñas
insulin = bInsulin + aInsulin

# Imprimir el valor de la insulina sin procesar
print("Imprimir el valor de la insulina sin procesar")
print(preproInsulin)

# Imprimir una cadena a
print("La secuencia de insulina, cadena a: " + aInsulin)

## Calcularemos los pesos de cada molécula
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19} 

# Contar cuántas veces aparece un aminoácido en la secuencia de insulina

aminoacidos = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T','V', 'W', 'Y']

conteo = {}

for x in aminoacidos:
    # Creo un elemento del diccionario con la letra y su cantidad de aparaciones
    conteo[x] = insulin.count(x.lower())

# Sumar el peso de cada uno
suma = 0
for x in aminoacidos:
    peso = conteo[x] * aaWeights[x]
    
    #suma = suma + peso
    suma += peso

print("El valor suma es", suma)

molecularWeightInsulin = suma

molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))

