cantantes = ["2PAC","EPTORS UNO","ACZINO","EMINEM"]
numeros = [1,2,5,8,3]

#ordena una lista
# print(numeros)
# numeros.sort()
# print(numeros)

#agregar elementos una lista
cantantes.append("50cent")
print(cantantes)
cantantes.insert(1,"snoop dog")
print(cantantes)

#eliminar elementos
cantantes.pop(1)
print(cantantes)
cantantes.remove("50cent")
print(cantantes)

#Voltear una lista
cantantes.reverse()
print(cantantes)

#buscar si un dato esta en la lista
print("EMINEM" in cantantes)

#cantidad de datos en una lista
print(len(cantantes))

#cantidad de veces que aparece un elemnto en la lista
print(cantantes.count("EMINEM"))

#CONSEGUIR EL INDICE
print(cantantes.index("EMINEM"))

#unir listas
cantantes.extend(numeros)
print(cantantes)