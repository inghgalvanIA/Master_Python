"""

FOR
for variable in elemento_iterable(lista,rango,tupla)
    Bloque de instrucciones
    
"""
contador = 0
resultado = 0

for contador in range(0,10):
    print("voy en el numero " + str(contador))
    resultado += contador

print(f"el resultado de la suma de todos es {resultado}")

