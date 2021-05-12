import datetime

# imprimir el dida de  hoy
print(datetime.date.today())

#obtener fecha completa

fecha_completa = datetime.datetime.now()

print(fecha_completa)

#si solo quiero obtener un dato ejemplo año

print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)
print(fecha_completa.hour)
print(fecha_completa.second)

#tiempo en unix
print(datetime.datetime.now().timestamp())

