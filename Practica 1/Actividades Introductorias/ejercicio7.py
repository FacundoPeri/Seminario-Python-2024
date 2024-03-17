# Escribe un programa que tome una lista de números enteros como entrada del usuario.
# Luego, convierte cada número en la lista a string y únelos en una sola cadena,
# separados por guiones ('-'). Sin embargo, excluye cualquier número que sea múltiplo
# de 3 de la cadena final.

lista = []

print('====== Se Leera una Lista de numeros ======')
print('La lectura finalizara al ingresar 0')
num = int(input('Ingrese un numero: '))
while (num != 0) :
    lista.append(num)
    num = int(input('Ingrese otro numero: '))
print('=========== Finalizo la lectura ===========')

cadena = ''
for num in lista:
    if (num % 3 != 0): cadena += str(num) + '-'
print(f'Lista sin multiplos de 3: {cadena[:-1]}')