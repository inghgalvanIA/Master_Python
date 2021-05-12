"""

lo correcto es que las funciones retornen un cvalor de preferencia con
un return

"""

def calculadora(num_1,num_2, basicas=False):
    suma = num_1 + num_2
    resta = num_1 - num_2
    multi = num_1 * num_2
    div = num_1 / num_2

    cadena = ""
    if basicas != False:
        cadena += "Suma: "+str(suma)
        cadena += "\n"
        cadena += "Resta: "+str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: "+str(multi)
        cadena += "\n"
        cadena += "Divicion: "+str(div)
        cadena += "\n"

    return cadena

print(calculadora(3, 5))