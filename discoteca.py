from datetime import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    return ano_atual - ano_nascimento

def verifica_acesso():
    escolha = input("Escolha '1' para inserir sua data de nascimento ou '2' para inserir sua idade: ")

    if escolha == '1':
        ano_nascimento = int(input("Por favor, digite o ano do seu nascimento (AAAA): "))
        idade = calcular_idade(ano_nascimento)
    elif escolha == '2':
        idade = int(input("Por favor, digite sua idade: "))
    else:
        print("Opção inválida.")
        return

    if idade >= 18:
        print("¡Bem-vindo/a à discoteca!")
    else:
        print("Desculpe, você é menor de idade e não pode entrar na discoteca.")

verifica_acesso()



