def getNombre(nombre):
    texto = f"el nombre del usuario es: {nombre}"
    return texto

def getApellido(apellido_paterno,apellido_materno):
    texto_apellidos = f"el apellido paterno: {apellido_paterno} el apellido materno: {apellido_materno}" 
    return texto_apellidos

def devuelveTodo(nombre,apellido_paterno,apellido_materno):
    texto_final = getNombre(nombre) + "\n" + getApellido(apellido_paterno, apellido_materno)
    return texto_final

print(devuelveTodo("Hèctor", "Galvàn", "Rivas"))