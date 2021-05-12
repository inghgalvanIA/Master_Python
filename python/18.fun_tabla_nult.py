numero = int(input("¿que tabla de multiplicar deseas saber?"))

def tabla_mult(num):
    print(f"la tabla de multiplicar {num}")
    contador = 0
    while contador <= 9:
        contador += 1
        resultado = contador * num
        print(f"{num} x {contador} = {resultado}")


tabla_mult(numero)