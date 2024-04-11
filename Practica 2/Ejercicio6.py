frase = input("Ingrese una frase: ")
palabra = input("Ingrese una palbra: ").lower()
palabras = frase.lower().split()

print(f"La palabra aparece {palabras.count(palabra)} veces en la frase.")
