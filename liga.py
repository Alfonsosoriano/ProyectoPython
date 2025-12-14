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
