## Dadas dos cadenas ingresadas desde el teclado, imprimir aquella que tenga más caracteres.
cadena_1 = input("Ingrese una cadena: ")
cadena_2 = input("Ingrese otra cadena: ")

if (len(cadena_1) > len(cadena_2)) : print(cadena_1)
elif (len(cadena_2) > len(cadena_1)) : print(cadena_2)
else : print("Ambas cadenas tienen la misma longitud")