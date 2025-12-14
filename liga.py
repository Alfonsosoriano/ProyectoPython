import csv

def LeerPartidos(ruta="liga.csv"):
    """Lee el fichero CSV y devuelve una lista de diccionarios."""
    partidos = []
    with open(ruta, newline='', encoding='utf-8') as f:
        lector = csv.reader(f)
        encabezados = next(lector) 
        for fila in lector:
            partido = {}
            for i in range(len(encabezados)):
                partido[encabezados[i]] = fila[i]
            partidos.append(partido)
    return partidos

def Equipos(datosliga):
    """Devuelve un conjunto con todos los equipos de la liga."""
    equipos = set()
    for partido in datosliga:
        equipos.add(partido['Team 1'])
        equipos.add(partido['Team 2'])
    return equipos

def QuienGana(resultado):
    """Indica quién gana un partido según el resultado."""
    partes = resultado.split('-')
    goles_local = int(partes[0])
    goles_visitante = int(partes[1])

    if goles_local == goles_visitante:
        return 0
    if goles_local > goles_visitante:
        return 1
    return -1

def Puntos(info):
    """Calcula los puntos a partir de ganados y empatados."""
    ganados = info[0]
    empatados = info[1]
    return ganados * 3 + empatados
