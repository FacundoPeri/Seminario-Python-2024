word = input("Ingresá una palabra: ")
if "a" in word and "n" in word:
    print("Hay al menos una letra a y al menos una letra n.")
elif "a" in word:
    print("Hay al menos una letra a.")
elif "n" in word:
    print("Hay al menos una letra n.")
else:
    print("No hay letras a ni letras n. ")