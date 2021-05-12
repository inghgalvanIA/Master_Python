from io import open
import pathlib

#abrir o crear un archivo si no existe

archivo = open("./prueba_fichero.txt","w+")
archivo.write("Esto es un texto desde python")

print(archivo)
