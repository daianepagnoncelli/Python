edad = int(input("Por favor, ingresa tu edad: "))

def verifica_edad():
    #try:
        if edad >= 18:
            print("¡Bienvenido/a a la discoteca!")
        else:
            print("Lo siento, eres menor de edad. No puedes ingresar a la discoteca.")
    #except:
        #print("Por favor, ingresa un número válido para la edad.")

verifica_edad()


