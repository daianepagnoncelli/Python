# Almacena la secuencia de preproinsulina humana en una variable llamada preproinsulina:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Almacena los elementos restantes de la secuencia de insulina humana en variables:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bInsulin + aInsulin

# Diccionario con los valores de pKR para aminoácidos específicos.
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}

# Conteo de aminoácidos en la secuencia de insulina.
seqCount = {x: float(insulin.count(x)) for x in ['y', 'c', 'k', 'h', 'r', 'd', 'e']}
print("Conteo de aminoácidos en la secuencia de insulina:")
print(seqCount)

# Inicialización del pH en 0.
pH = 0

# Bucle while para calcular la carga neta en el rango de pH de 0 a 14.
while (pH <= 14):
    # Fórmula para calcular la carga neta.
    netCharge = (
        +(sum({x: ((seqCount[x] * (10 ** pKR[x])) / ((10 ** pH) + (10 ** pKR[x]))) \
               for x in ['k', 'h', 'r']}.values()))
        - (sum({x: ((seqCount[x] * (10 ** pH)) / ((10 ** pH) + (10 ** pKR[x]))) \
                for x in ['y', 'c', 'd', 'e']}.values()))
    )
    
    # Imprime el valor de pH y la carga neta con dos decimales de precisión.
    print('{0:.2f}'.format(pH), netCharge)
    
    # Incrementa el valor de pH en uno para la próxima iteración del bucle while.
    pH += 1
