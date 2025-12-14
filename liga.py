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

def InfoEquipos(datosliga, equipos):
    """Devuelve una lista con la información de cada equipo."""
    info = []

    for equipo in equipos:
        ganados = 0
        empatados = 0
        perdidos = 0

        for partido in datosliga:
            resultado = QuienGana(partido['FT'])

            if partido['Team 1'] == equipo:
                if resultado == 1:
                    ganados = ganados + 1
                elif resultado == 0:
                    empatados = empatados + 1
                else:
                    perdidos = perdidos + 1

            if partido['Team 2'] == equipo:
                if resultado == -1:
                    ganados = ganados + 1
                elif resultado == 0:
                    empatados = empatados + 1
                else:
                    perdidos = perdidos + 1

        puntos = Puntos([ganados, empatados, perdidos])
        info.append((equipo, ganados, empatados, perdidos, puntos))

    return info


def Clasificacion(datos):
    """Ordena los equipos por puntos."""
    ordenados = []

    for equipo in datos:
        insertado = False
        for i in range(len(ordenados)):
            if equipo[4] > ordenados[i][4]:
                ordenados.insert(i, equipo)
                insertado = True
                break
        if not insertado:
            ordenados.append(equipo)

    return ordenados


def impClasificacion(liga):
    """Imprime la clasificación final por pantalla."""
    equipos = Equipos(liga)
    datos = InfoEquipos(liga, equipos)
    clasificacion = Clasificacion(datos)

    print("CLASIFICACIÓN FINAL")
    print("Pos  Equipo                 G   E   P   Pts")
    print("---------------------------------------------")

    pos = 1
    for fila in clasificacion:
        equipo = fila[0]
        ganados = fila[1]
        empatados = fila[2]
        perdidos = fila[3]
        puntos = fila[4]

        print(f"{pos:<4} {equipo:<22} {ganados:<3} {empatados:<3} {perdidos:<3} {puntos:<3}")
        pos = pos + 1


if __name__ == '__main__':
    datos_liga = LeerPartidos()
    impClasificacion(datos_liga)
