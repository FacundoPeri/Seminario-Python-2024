#Queremos ingresar un número desde el teclado e imprimir si es múltiplo de 2, 3 o 5.

numero = int(input("Ingrese un numero: "))

if (numero % 2 == 0): print("Es multiplo de 2")
elif (numero % 3 == 0): print("Es multiplo de 3")
elif(numero % 5 == 0): print("Es multiplo de 5")
else : print("No es multiplo de 2,3 ni 5")