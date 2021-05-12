print("********listado de contactos*********")

contactos = [["Antonio","jefe de sistemas","antogiog@gmail.com"],
            ["jesus","Dir. Mercadotecnia","jruiz@gmail.com"],
            ["Arturo","Aux. admin","arod@gmail.com"]
            ]

print(contactos)
#para accerder al email de jesus
print(contactos[1][2])
#para acceder al puesto de Arturo
print(contactos[2][1])

#lista de contactos

for contacto in contactos:
    
        print(f"Nombre: {contacto[0]}")
        print(f"Puesto: {contacto[1]}")
        print(f"Email: {contacto[2]}")
        print("**************************")