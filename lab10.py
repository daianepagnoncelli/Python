import re  # Importa expressões regulares

# Lê o arquivo com a sequência original
with open('preproinsulin-seq-original.txt', 'r') as arquivo:
    sequencia = arquivo.read()

# Remove 'ORIGIN', '1', '61', '//', espaços e quebras de linha
sequencia_limpa = re.sub(r'ORIGIN|\d+|\/\/|\s+', '', sequencia)

# Extrai os aminoácidos 1-24 e verifica se possui 24 caracteres
lsinsulin_sequence = sequencia_limpa[:24]
with open('lsinsulin-seq-clean.txt', 'w') as novo_arquivo:
    novo_arquivo.write(lsinsulin_sequence)
if len(lsinsulin_sequence) == 24:
    print("O arquivo lsinsulin-seq-clean.txt possui 24 caracteres.")
else:
    print("O arquivo lsinsulin-seq-clean.txt não possui 24 caracteres.")

# Extrai os aminoácidos 25-54 e verifica se possui 30 caracteres
binsulin_sequence = sequencia_limpa[24:54]
with open('binsulin-seq-clean.txt', 'w') as novo_arquivo:
    novo_arquivo.write(binsulin_sequence)
if len(binsulin_sequence) == 30:
    print("O arquivo binsulin-seq-clean.txt possui 30 caracteres.")
else:
    print("O arquivo binsulin-seq-clean.txt não possui 30 caracteres.")

# Extrai os aminoácidos 55-89 e verifica se possui 35 caracteres
cinsulin_sequence = sequencia_limpa[54:89]
with open('cinsulin-seq-clean.txt', 'w') as novo_arquivo:
    novo_arquivo.write(cinsulin_sequence)
if len(cinsulin_sequence) == 35:
    print("O arquivo cinsulin-seq-clean.txt possui 35 caracteres.")
else:
    print("O arquivo cinsulin-seq-clean.txt não possui 35 caracteres.")

# Extrai os aminoácidos 90-110 e verifica se possui 21 caracteres
ainsulin_sequence = sequencia_limpa[89:110]
with open('ainsulin-seq-clean.txt', 'w') as novo_arquivo:
    novo_arquivo.write(ainsulin_sequence)
if len(ainsulin_sequence) == 21:
    print("O arquivo ainsulin-seq-clean.txt possui 21 caracteres.")
else:
    print("O arquivo ainsulin-seq-clean.txt não possui 21 caracteres.")
