#Ejemplo tablas de multiplicar
print("################# tabla de multiplicar ##################")



num = int(input("¿cual tabla deseas saber?"))
#list = [1,2,3,4,5,6,7,8,9,10]

if num > 0:

    for contador in range(1,11):
        valor = num * contador
        print(f"{num} x {contador} = {valor}")
    else:
        print("Tabla finaliza")
else:
    print("No esta disponible la tabla del 0")