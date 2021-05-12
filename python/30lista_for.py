peliculas = ["batman","spiderman 2","el señor de los anillos","avengers","bambi","mision imposible"]


nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("ingresa una nueva pelicula: ")
    if nueva_pelicula == "parar":
        continue
    else:
        peliculas.append(nueva_pelicula)




print("********listado de peliculas***********")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1} {pelicula}")