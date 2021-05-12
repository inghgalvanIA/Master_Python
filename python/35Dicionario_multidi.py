contactos =[
    {
        "nombre":"Antonio",
        "apellido":"Gonzalez",
        "email":"agonzalez"

    },
    {
        "nombre":"Adriana",
        "apellido":"Gonzalez",
        "email":"azulema"

    }
]

contactos[0]["nombre"] = "Ezequiel"
print(contactos[0]["nombre"])

for contacto in contactos:
    print("Nombre: " + contacto["nombre"])
    print("email: " + contacto["email"])