## Determinar si una palabra ingresada desde el teclado es un sustantivo propio o no.
import string

palabra =  input("Ingrese una palabra: ")

if (palabra[0] in string.ascii_uppercase): print("Es sustantivo propio")
else: print("No es sustantivo propio")