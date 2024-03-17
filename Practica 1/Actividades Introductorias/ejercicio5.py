# Implementa un programa que solicite al usuario que ingrese una lista de números.
# Luego, imprime la lista pero detén la impresión si encuentras un número negativo.
# Nota: utilice la sentencia break cuando haga falta.

print('====== Se Leera una Lista de numeros ======')
print('La lectura finalizara al ingresar 0')

lista = []
num = int(input('Ingrese un numero: '))

while (num != 0) :
    lista.append(num)
    num = int(input('Ingrese otro numero: '))

print()
print('====== Se imprimira la lista hasta que se encuentre un numero negativo ======')
for num in lista:
    if num < 0 : break
    print(num)