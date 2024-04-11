import string

cadena = input("- Ingrese una palabra o frase: ").lower()

sin_espacios = cadena.replace(" ","")
no_repetidos = 0
for c in list(sin_espacios):
    if ((c in string.ascii_letters) and (cadena.count(c) == 1)): no_repetidos += 1

if (no_repetidos == len(sin_espacios)) : print("------ La cadena es heterogama ------")
else : print("------ La cadena no es heterogama ------")

# Forma mas eficiente:

cadena = input("- Ingrese una palabra o frase: ").lower()

sin_espacios = cadena.replace(" ", "")
caracteres_unicos = set(sin_espacios)

if len(sin_espacios) == len(caracteres_unicos):
    print("------ La cadena es heterogama ------")
else:
    print("------ La cadena no es heterogama ------")