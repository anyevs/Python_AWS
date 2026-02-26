# Para crear una lista se usan []
# Creamos la lista myFruitList y dentro de ella guardamos las siguientes frutas: apple, banana y cherry
myFruitList = ["apple", "banana", "cherry"]

# Imprimimos la lista de frutas completa
print(myFruitList)

# Imprimimos rl tipo de dato que es myFruitList con type ()
print(type(myFruitList))

#Imprimimos el valor que esta en la primera posicion de la lista myFruitList (Este valor es "apple")
print(myFruitList[0])

#Imprimimos el valor que esta en la segunda posicion de la lista myFruitList (Este valor es "banana")
print(myFruitList[1])

#Imprimimos el valor que esta en la tercera posicion de la lista myFruitList (Este valor es "cherry")
print(myFruitList[2])

# Vamos a cambiar el valor de la lista en su posicion 2 que antes era "cherry" y ahora va a ser "orange"
myFruitList[2] = "orange"

# Impeimimos la lista completa con el cambio
print(myFruitList)

# Para crear una tupla se usan ()
# Creamos la tupla myFinalAnswerTupke y dentro de ella guardamos las siguientes frutas: apple, banana y pineapple
myFinalAnswerTuple = ("apple", "banana", "pineapple")

#Imprimimos la tupla completa
print(myFinalAnswerTuple)

# Imprimimos el tipo de dato de myFinalAnswerTuple 
print(type(myFinalAnswerTuple))

# Imprimimos el primer valor de la tupla que es "apple"
print(myFinalAnswerTuple[0])

# Imprimimos el segundo valor de la tupla que es "banana"
print(myFinalAnswerTuple[1])

# Imprimimos el tercer valor de la tupla que es "pineapple"
print(myFinalAnswerTuple[2])

# Para crear un diccionario se utilizan {} y dentro de ellas se va a crear una clave y un valor. La clave y el valor van separados por : y luego de cada clave-valor se separa del siguiente usando una ,
# Creamos el diccionario myFavoriteFruitDictionary con las siguientes claves: "Akua", "Saanvi" y "Paulo". Con sus correspoondientes valores: "apple", "banana", "pineapple"
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

# Imprimimos el diccionario completo
print(myFavoriteFruitDictionary)

# Implimimos el tipo de variable de myFavoriteFruitDictionary
print(type(myFavoriteFruitDictionary))

# Imprimimos el valor de la clave "Akua"
print(myFavoriteFruitDictionary["Akua"])

# Imprimimos el valor de la clave "Saanvi"
print(myFavoriteFruitDictionary["Saanvi"])

# Imprimimos el valor de la clave "Paulo"
print(myFavoriteFruitDictionary["Paulo"])