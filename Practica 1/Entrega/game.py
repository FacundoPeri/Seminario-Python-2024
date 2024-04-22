import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo","inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de errores permitidos
max_fails = 10
fails = 0

# Lista para almacenar las letras adivinadas
guessed_letters = []


print("¡Bienvenido al juego de adivinanzas!")
print("""Seleccione una dificultad:
    1 - Facil
    2 - Normal
    3 - Dificil""")
dificultad = int(input("Ingrese una opcion: "))

letters = []
match dificultad:
    case 1:
        print('------ Se selcciono la dificultad Facil ------')
        guessed_letters = ['a','e','i','o','u']
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
        word_displayed = "".join(letters)
    case 2:
        print('------ Se selcciono la dificultad Media ------')
        guessed_letters = [secret_word[0],secret_word[-1]]
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append("_")
        word_displayed = "".join(letters)
    case 3:
        print('------ Se selcciono la dificultad Dificil ------')
        word_displayed = "_" * len(secret_word)

print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
# Mostrarla palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")


while (fails < max_fails):

    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    if letter in guessed_letters:
        # Verificar si la letra ya ha sido adivinada
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue
    elif (letter == '') or (letter == ' '):
        # Verifica que la letra no sea un caracter vacio o un espacio.
        print("ERROR : No se ingreso ninguna letra.")
        continue
    else:
        # Agregar la letra a la lista de letras adivinadas
        guessed_letters.append(letter)
 
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word: 
       print("¡Bien hecho! La letra está en la palabra.")
    else: 
       print("Lo siento, la letra no está en la palabra.")
       fails += 1
 
    letters = []
    # Mostrar la palabra parcialmente adivinada
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")

    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")

    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta:{secret_word}")
        break


else:
    print(f"¡Oh no! Has alcanzado los {max_fails} errores.")
    print(f"La palabra secreta era: {secret_word}")