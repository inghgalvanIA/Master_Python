""" 
variable local: se defiene dentro de la funcion y no 
se puede usar fuera de ella, solo esyan disponibles dentro ano ser que hagamos return

varable global:son las que se declaran fuera de una funcion y estan disponibles dentro y fuera
de ellas

""" 

frase = "Hace mucho tiempo que ya no soy el mismo"

print(frase)

def holaMundo():
    frase = "Hola mundo!!!"
    print(frase)

holaMundo()