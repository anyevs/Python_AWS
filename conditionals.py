# Se va a crear un validador para saber si podemos entrar o no a una fiesta. Es importante agregar que para entrar a la fiesta debes ser mayor de edad
# Se crea la variable edad y en ella se va a guardar lo que escriba el usuario
edad = input("Escriba su edad: ")

#convertimos la variable entrada a entero debido a que cuando se escribe por consola el valor que se guarda es el de un texto
edad = int(edad)

# Vamos a comparar si la edad es mayor o igual a 18 años
if edad >= 18 :
    # Imprime que lo deja entrar
    print("Puede entrar")
else: 
    #Si no se cumple la condicion que es mayor de 18 años imprime "no puede entrar"
    print("No puede entrar")
    
# Ahora se va a validar si la persona es mayor de edad y ademas si la persona tiene mas de $600
# Se crea la variable edad y en ella se guarda lo que escriba el usuario
edad = input("Escriba su edad: ")

# Convertimos la variable entrada a entero debido a que cuando se escribe por consola el valor que se guarda es el de un texto
edad = int(edad)

# Se crea la variable dinero y en ella se guarda lo que escriba el usuario
dinero = input("Escriba cuanto dinero tiene: ")

# Convertimos la variable entrada a entero debido a que cuando se escribe por consola el valor que se guarda es el de un texto
dinero = int(dinero)

# Vamos a comparar si la edad es mayor o igual a 18 años
if edad >= 18 :
     # Verificamos si cuenta con el dinero
     if dinero >= 600 :
         # Imprime que lo deja entrar
        print("Puede entrar")
     else: 
        # Como no tiene el dinero no puede entrar
        print("No puede entrar")
else:
    # Como no tiene la edad no puede entrar
    print("No puede entrar")
    
# Vamos a comparar si la edad es mayor o igual a 18 años - version 2
if edad >= 18 & dinero >= 600 :
         # Imprime que lo deja entrar
        print("v2 Puede entrar")
else:
        # Como no tiene el dinero no puede entrar
        print(" v2 No puede entrar")

#---------------------------------------------------------------
# CONDICIONAL CON MULTIPLES COMPARACIONES
# Creamos la variable llamada dinero
dinero  = input("Escriba el dinero con el que cuenta: ")

dinero = int(dinero)

if dinero < 100 :
    print("Le compro unas galletas")
elif dinero >= 100 and dinero <=200 :
    print("Le compro unos chocolates")
elif dinero > 200 and dinero <= 300 :
    print("Le compro unas picafresas")
else: 
    print("le compro un peluche")
    
#----------Laboratorio-----------------------
# Creamos la variable userReply y guardamos lo que diga el usuario
userReply = input("Do you need to ship a package? (Enter yes or no) ")

# Si lo que hay dentro de la variable es exactamente igual a yes
if userReply == "yes":
    # Imprime que nos puede ayudar
    print("We can help you ship that package!")
# De lo contrario dice que vuelva pronto    
else:
    print("Please come back when you need to ship a package. Thank you.")  
    
# En la variable userReply vamos a guardar una de estas opciones: stamps, envelope, or copy
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
# Si la variable es exactamente igual a stamps
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
# Si la variable es exactamente igual a envelope
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
# Si la variable es exactamente igual a copias
elif userReply == "copy":
    #Se crea la variable copies y se almacena el numero de copias que desea crear el usuario
    copies = input("How many copies would you like? (Enter a number) ")
    #  se imprime el numero de copias
    print("Here are {} copies.".format(copies))
else:
    #Imprime el mensaje de despedida
    print("Thank you, please come again.")