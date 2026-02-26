# Se importa una libreria siempre al principio del codigo
import random
# Un ciclo while es un bucle que va a recorrer hasta que no se cumpla la condicion
# Se crea la variable numero y se ele pide al usuario que escriba el numero 0
numero = input("Escriba el numero 0: ")

# Convertimos la variable numero de string a entero
numero = int(numero)

# se verifica que la variable numero sea menor a 10
while numero < 10 :
    # se incrementa el valor del numero
    numero = numero + 1
    # si numero es menor a 10 se imprime su valor
    print(numero)
    

#-----------------------------------------------------------------------------
# Vamos a construir algo que nos muestre las tablas de multiplicar de un numero
# Se crea la variable numero y se ele pide al usuario que escriba el numero 0
numero = input("Escriba un numero ")
# Convertimos la variable numero de string a entero
numero = int(numero)
  # multiplicador
multiplicador = 0

# se verifica que la variable numero sea menor a 10
while multiplicador < 10 :
    # se incrementa el valor del multiplicador
    multiplicador = multiplicador + 1
    # valor de multiplicacion
    multiplicacion = numero * multiplicador
    # si numero es menor a 10 se imprime su valor
    print(numero, "*", multiplicador, "=", multiplicacion)
    
#-------------Laboratorio------------------------------------------
# se realizan 2 impresiones
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
    
# la libreria random genera num aleatorios desde un num inicial hasta uno final
number = random.randint(1,10)

# Se crea la variable isGuessRight y se guarda un valor booleano (False)
isGuessRight = False

#Mientras la variable isGuessRight sea diferente de verdadero se ejecuta el codigo
while isGuessRight != True:
    # se crea la variable guess y se guarda dentro lo que escriba el usuario
    guess = input("Guess a number between 1 and 10: ")
    # mientras el valor de guess sea un entero exactamente igual al valor de la variable number
    if int(guess) == number:
        # imprime que ganamos 
        print("You guessed {}. That is correct! You win!".format(guess))
        # la variable isGuessRigth se pasa a verdadero para terminar el ciclo while
        isGuessRight = True
    # Si la variable guess no es exactamente igual a la variable isGuessRigth imprime
    else:
        # "Intentalo de nuevo"
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))