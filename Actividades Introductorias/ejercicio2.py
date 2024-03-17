# Haz un programa que pida al usuario que ingrese una temperatura en grados Celsius y
# luego convierta esa temperatura a grados Fahrenheit, mostrando el resultado.

grCelsius = float(input('Ingrese una temperatura en grados celsius: '))
print('La temperatura en celsius es ',grCelsius,'°')
grFarenheit = (grCelsius * 9/5) + 32
print('El equivalente en farenheit es ', grFarenheit,'°')