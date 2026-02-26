# La libreria csv nos permite trabajar con archivos separados por , 
import csv
# La libreria copy nos permite tomar datos de un archivo y usarlos dentro de un programa 
import copy

# se crea el diccionario myVehicle
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# se crea un ciclo for para imprimir cada una de las clave valor que hay dentro del diccionario
for key, value in myVehicle.items():
    # se imprime la clave valor
    print("{} : {}".format(key,value))

# se crea la lista myInventoryList    
myInventoryList = []

# se abre el archivo car_fleet.csv y se guarda dentro de la variable csvFile
with open('car_fleet.csv') as csvFile:
    # se lee el archivo csvReader donde su delimitador son las ,
    csvReader = csv.reader(csvFile, delimiter=',')  
    # se crea la variable linecount y se le asigna el valor de 0
    lineCount = 0  
    # se lee cada una de las lineas del archivo csvReader
    for row in csvReader:
        # si el valor de las lineas es 0 
        if lineCount == 0:
            # imprime el nombre de la columna
            print(f'Column names are: {", ".join(row)}')
            # y se aumenta en 1 el valor de lineCount
            lineCount += 1  
        # si el valor de las lineas no es 0    
        else: 
            # se imprime en cada una de las claves la posicion que fue separada por comas anteriormente
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            # se copia el valor de las variables dentro del diccionario myVehicle
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            # se agrega a la lista un vehiculo
            myInventoryList.append(currentVehicle)  
            # se aumenta en 1 el valor de lineCount
            lineCount += 1  
    # se imprime el total de lineas leidas  
    print(f'Processed {lineCount} lines.')
    
# se crea un for para imprimir cada vehiculo de la lista
for myCarProperties in myInventoryList:
    # se imprimen los datos de cada vehiculo
    for key, value in myCarProperties.items():
    # se imprime la llave valor
        print("{} : {}".format(key,value))
     # se imprime un separador
        print("-----")