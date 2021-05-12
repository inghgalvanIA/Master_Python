numero = int(input("¿que tabla deseas obtener?"))
multiple = 0

if numero > 0 and numero < 11:
    while multiple <= 9:
        multiple += 1
        resultado = numero * multiple
        print(f"{numero} x {multiple} = {resultado}")
else:
    print("El numero seleccionado no tiene tabla")