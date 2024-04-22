# Dado una letra ingresada por el teclado, queremos saber si es mayúscula o minúscula.}
import string
c = input("Ingrese una letra por teclado: ")

if (c in string.ascii_lowercase): print("Es minuscula")
elif (c in string.ascii_uppercase): print("Es mayuscula")
else: print("No es un caracter del alfabeto")

