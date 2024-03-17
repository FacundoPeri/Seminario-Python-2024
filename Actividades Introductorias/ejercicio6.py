# Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas listas, una
# con los número pares y otras con los que son impares. Imprima las listas al terminar de
# procesarlas.

lista = [43,34,67,44,867,77,123,12]
listaPares = []
listaImpares = []


for num in lista:
    if (num % 2 == 0) : listaPares.append(num)
    else : listaImpares.append(num)

print()
print("Lista: ")
for num in lista:
    print(num)

print()
print("Pares: ")
for num in listaPares:
    print(num)

print()
print("Impares: ")
for num in listaImpares:
    print(num)