import string

text = """ La brecha salarial alcanzó el 27,7%: las mujeres ocupadas
debieron trabajar 8 días y 10 horas más que los varones ocupados para
ganar lo mismo que ellos en un mes. """

cant_mayus = 0
cant_minus = 0

for c in text: 
    if (c in string.ascii_lowercase) : cant_minus += 1
    elif (c in string.ascii_uppercase) : cant_mayus += 1

print(f"La cantidad de minisculas del texto es {cant_minus}")
print(f"La cantidad de mayusculas del texto es {cant_mayus}")


