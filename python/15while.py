"""
Bucle while

Estructura de control que itera o repita la ejecucion de una
serue de instrucciones tantas veces como sea necesario, hatsa que deje de cumplirse la condicion

while condicion:
    bloque de instrucciones
"""
contador = 0
contador_dos = 0
muestrame = str(0)

while contador <= 99:
    contador += 1
    print(f"estoy en el numero {contador} ")

print("##################################")

while contador_dos <= 99:
    contador_dos += 1
    muestrame = muestrame + "  ," + str(contador_dos)

print(muestrame)