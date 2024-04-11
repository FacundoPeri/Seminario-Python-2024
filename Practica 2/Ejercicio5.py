import string

article = """ título: Experiences in Developing a Distributed Agentbased Modeling Toolkit with Python Version 3
resumen: Distributed agent-based modeling (ABM) on high-performance 4 computing resources provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to wider adoption and utilization. 
Here we present our experiences in developing an initial implementation of Repast4Py, a Python-based distributed ABM toolkit.
We build on our experiences in developing ABM toolkits, including Repast for High Performance Computing (Repast HPC), to identify the key elements of a useful distributed ABM toolkit.
We leverage the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling system that can exploit the largest HPC resources and emerging computing architectures. """

oraciones = article.split("\n")

#Extraigo el titulo
titulo = oraciones.pop(0)

dificultad = {
    "Facil" : 0,
    "Aceptable" : 0,
    "Dificil" : 0,
    "Muy Dificil" : 0
    }
for x in range(len(oraciones)) : 
    # Divido cada oracion en palabras
    oraciones[x] = oraciones[x].split()
    
    # Elimino las apariciones de nmeros
    for y in range(len(oraciones[x])):     
        if (oraciones[x][y] in string.digits) : oraciones[x].pop(y)

    # Actualizo la cantidad de oraciones por dificultad de lectura
    if (len(oraciones[x]) <= 12) : dificultad["Facil"] += 1
    elif ((len(oraciones[x]) >= 13) and (len(oraciones[x]) <= 17)) : dificultad["Aceptable"] += 1
    elif ((len(oraciones[x]) >= 18) and (len(oraciones[x]) <= 25)) : dificultad["Dificil"] += 1
    else : dificultad["Muy Dificil"] += 1

if (len(titulo) <= 10) : print("El titulo cumple las especificaciones")
else: print("El titulo no cumple las especificaciones")

print("Cantidad de oraciones segun su dificultad de lectura:")
print(f"- Faciles: {dificultad["Facil"]}")
print(f"- Aceptables: {dificultad["Aceptable"]}")
print(f"- Dificiles: {dificultad["Dificil"]}")
print(f"- Muy dificiles: {dificultad["Muy Dificil"]}")



    








