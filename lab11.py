# Almacena la secuencia humana de preproinsulina en una variable llamada preproinsulin:
preproinsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Almacena los elementos restantes de la secuencia de insulina humana en variables:
lsinsulina = preproinsulin[:24]
binsulina = preproinsulin[24:54]
cinsulina = preproinsulin[54:89]
ainsulina = preproinsulin[89:]

# Concatena las secuencias bInsulina y aInsulina
insulina = binsulina + ainsulina

# Imprime la secuencia de preproinsulina e insulina humana en la consola usando comandos print():
print("La secuencia de preproinsulina humana:")
print(preproinsulin)

print("La secuencia de insulina humana, cadena a:")
print(ainsulina)

print("La secuencia de insulina humana, cadena b:")
print(binsulina)

print("La secuencia de insulina humana, cadena c:")
print(cinsulina)

print("La secuencia de insulina humana (cadenas b + a):")
print(insulina)

# Calcula el peso molecular de la insulina
# Crea una lista de los pesos de los aminoácidos (AA)
pesosAA = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}

# Cuenta el número de cada aminoácido
conteoAAInsulina = ({x: float(insulina.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})

# Multiplica el conteo por los pesos
pesoMolecularInsulina = sum({x: (conteoAAInsulina[x]*pesosAA[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())

print("El peso molecular aproximado de la insulina: " +
str(pesoMolecularInsulina))

pesoMolecularInsulinaReal = 5807.63
print("Porcentaje de error: " + str(((pesoMolecularInsulina - pesoMolecularInsulinaReal)/pesoMolecularInsulinaReal)*100))
