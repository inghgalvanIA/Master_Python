list_num = [1,2,3,4,5,6,7,8,9,10]

def tabla_mult(num):
    print(f"la tabla de multiplicar {num}")
    contador = 0
    while contador <= 9:
        contador += 1
        resultado = contador * num
        print(f"{num} x {contador} = {resultado}")

def todas_tablas(list_num):
    for index in list_num:
        result = tabla_mult(index)
        

todas_tablas(list_num)
