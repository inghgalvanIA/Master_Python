nombre = input("Introduce tu nombre")
edad = int(input("Ingresa tu edad"))

def saludar(nombre,edad):
    mensaje = None
    if edad >= 18:
        mensaje = "Eres mayor de edad"
    else:
        mensaje = "Eres menor de edad"
    return "Hola " + nombre + " tienes " + str(edad) + " y " + mensaje

print(saludar(nombre,edad))