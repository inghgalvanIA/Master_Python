nombre = "Hector Galvan"

#funciones generales
#imprimir pantalla
print(nombre)
#expresar que tipo de dato es una variable
print(type(nombre))
#detectar un tipado en especifico isintance(nombre_variable,tipo)
comprobar = isinstance(nombre, str)
if comprobar:
    print("nombre es un string")

#limpiar espacios en un string
frase = "   mi contenido   "
print(frase)
print(frase.strip())

#eliminar variables

year = 2023
print(year)
del year
#print(year)

#comprobar una variable vacia

texto = "  ff  "
if len(texto) <= 0:
    print("la cadena esta vacia")
else:
    print("la cadena tiene string")

frase = "La vida es bella"

print(frase.find("vida"))