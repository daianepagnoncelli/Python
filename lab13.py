def getDoubleAlphabet(alphabet):
    # Duplica el alfabeto y lo devuelve
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

def getMessage():
    # Solicita al usuario un mensaje para encriptar
    stringToEncrypt = input("Por favor, ingresa un mensaje para encriptar: ")
    return stringToEncrypt

def getCipherKey():
    # Solicita al usuario una clave (número entero del 1 al 25)
    shiftAmount = input("Por favor, ingresa una clave (número entero del 1 al 25): ")
    return shiftAmount

def encryptMessage(message, cipherKey, alphabet):
    # Encripta el mensaje utilizando el cifrado César
    encryptedMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition % len(alphabet)]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

def decryptMessage(message, cipherKey, alphabet):
    # Descifra el mensaje utilizando el cifrado César
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
