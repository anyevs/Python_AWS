# Una funcion recibe parametros o variables para realizar una tarea especifica

# Creamos una funcion llamada suma

def suma (numero1, numero2):
    #Guardamos en la variable resultado el valor de la suma
    resultado = numero1 + numero2
    # Devolvemos el valor del proceso
    return resultado
    
# Creamos una variable A con lo que diga el usuario
a = input("Escriba un numero: ")

# Convertimos la variable a num
a = int(a)

# Creamos una variable b con lo que diga el usuario
b = input("Escriba un numero: ")

# Convertimos la variable a num
b = int(b)

# Llamamos a la funcion suma para obtener el resultado y la imprimimos
print(suma(a, b))

# -----------------------LABORATORIO--------------------------------
# La idea es “mover” cada letra del mensaje un número de posiciones (la clave).
# Por ejemplo, si la clave es 3: A -> D, B -> E, C -> F, etc.

# Esta función recibe un alfabeto (texto) y lo pega consigo mismo.
# Lo hacemos para poder “movernos” hacia adelante sin quedarnos sin letras.
# Ejemplo: "ABC" se vuelve "ABCABC".
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Esta función le pide al usuario que escriba un mensaje.
# Lo que el usuario escriba se guarda y luego se devuelve.
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt

# Esta función le pide al usuario una clave.
# La clave es un número del 1 al 25 que indica cuánto se moverán las letras.
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount
    
# Esta función hace el trabajo de encriptar.
# Recorre el mensaje letra por letra, busca cada letra en el alfabeto,
# le suma la clave para “moverla”, y va armando el mensaje encriptado.
def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    # Duplico el alfabeto para poder desplazar letras sin problemas
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    # Pido el mensaje al usuario
    myMessage = getMessage()
    print(myMessage)
    # Pido la clave al usuario
    myCipherKey = getCipherKey()
    print(myCipherKey)
    # Encripto el mensaje
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    # Desencripto el mensaje (para comprobar que vuelve al original)
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')
    
# Funcion desencriptar
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    # Aquí reviso cada letra del mensaje (ya en mayúsculas)
    for currentCharacter in uppercaseMessage:
        # Busco en qué posición está la letra dentro del alfabeto
        position = alphabet.find(currentCharacter)
        # Calculo la nueva posición sumando la clave
        newPosition = position + int(cipherKey)
        # Si la letra sí está en el alfabeto, cambio por la letra “movida”
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            # Si no es letra (por ejemplo espacio, número o símbolo), la dejo igual
            encryptedMessage = encryptedMessage + currentCharacter
    # Al final devuelvo el texto encriptado completo
    return encryptedMessage
    
# Funcion de desencriptar
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# Si no llamamos la función principal, no pasa nada.
# Esta línea es la que “arranca” el programa.
runCaesarCipherProgram()