
## Primer Inciso: Generar una estructura todas las estadísticas asociadas a cada jugador o jugadora.

def inciso_a():

    names = """ Agustin, Yanina, Andrés, Ariadna, Bautista, CAROLINA, CESAR, David, Diego, Dolores, DYLAN, 
    ELIANA, Emanuel, Fabián, Noelia, Francsica', FEDERICO, Fernanda, GONZALO, Nancy """
    goals = [0, 10, 4, 0, 5, 14, 0, 0, 7, 2, 1, 1, 1, 5, 6, 1, 1, 2, 0, 11]
    goals_avoided = [0, 2, 0, 0, 5, 2, 0, 0, 1, 2, 0, 5, 5, 0, 1, 0, 2, 3, 0, 0]
    assists = [0, 5, 1, 0, 5, 2, 0, 0, 1, 2, 1, 5, 5, 0, 1, 0, 2, 3, 1, 0]
    lista_nombres = names.split(", ")

    estadisticas = dict()
    for i in range(len(lista_nombres)):
        estadisticas[lista_nombres[i]] = {"Goles" : goals[i] , "Evitados" : goals_avoided[i] , "Asistencias" : assists[i]}

    return estadisticas

## Segundo Inciso:  Conocer el nombre y la cantidad de goles del goleador o goleadora. 

def inciso_b(estadisticas):
    max_goles = -1
    goleador = ''

    for jugador,datos in estadisticas.items():
        if (datos["Goles"] > max_goles):
            max_goles = datos["Goles"]
            goleador = jugador

    return goleador, max_goles

## Tercer Inciso: Conocer el nombre del jugador o jugadora más influyente, esto se consigue sumando goles a favor, goles evitados y cantidad de 
## asistencias. La particularidad es que los goles a favor, evitados y las asistencias NO valen lo mismo (es un promedio ponderado).

def inciso_c(estadisticas):
    mejor_promedio = -1.0
    influyente = ''

    for jugador, datos in estadisticas.items():
        promedio = (datos["Goles"] * 1.5) + (datos["Evitados"] * 1.25) + datos["Asistencias"]
        if (promedio > mejor_promedio): 
            mejor_promedio = promedio
            influyente = jugador

    return influyente

## Cuarto Inciso: Conocer el promedio de goles por partido del equipo en general. Dato: Se jugaron 25 partidos en la temporada.
def inciso_d(estadisticas, cant_partidos):
    cant_goles = 0

    for datos in estadisticas.values():
        cant_goles += datos["Goles"]

    promedio_goles = cant_goles / cant_partidos

    return promedio_goles


