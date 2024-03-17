# Cree un programa que dada una lista de números imprima sólo los que son pares.
# Nota: utilice la sentencia continue donde haga falta.

lista = [43,34,67,44,867,77,123,12]

for num in lista:
    if (num % 2 != 0) : continue
    print(num)