import numpy as np

#1 funcion que crea tableros de 10x10
def crear_tablero(tamaño=10):
    tablero = np.full((tamaño, tamaño), "_")
    return tablero


#2 funcion crear barcos (con posición inicial aleatoria, crear con if que queden dentro de rango/tablero, en crear flota comprobaré que no se solapen)
def crear_barco(eslora):
    barco = []
    pos_ini = (np.random.randint(10), np.random.randint(10))#creo la posición inicial de un barco al azar
    p = 1
    barco.append(pos_ini)
    dir = np.random.choice(("v", "h"))

    if dir == "v": #en el caso de que sea vertical, haces este bucle
        for pos in np.arange(eslora -1):
            barco.append((pos_ini[0] + p, pos_ini[1])) # le digo que dentro de la tupla, la primera posición (filas), es la posición 0, entonces sumale +1
            p = p + 1
    else:
        for pos in range(eslora -1):
            barco.append((pos_ini [0], pos_ini[1] + p))
            p = p + 1 
    return barco

#3 Función crear flota
def crear_flota():
    esloras_flota = [4, 3, 3, 2, 2, 2]
    flota = []
    for eslora in esloras_flota:
        flota.append(crear_barco(eslora))

    for barco in flota:
        for coor in barco:
            for i in coor:
                if i < 0 or i > 9:
                    print("generando flota de nuevo (fuera del tablero)")
                    return crear_flota()

    if hay_solape(flota):
        print("generando flota de nuevo (solapados)")
        return crear_flota()

    return flota


#4 funcion que coloca los barcos en el tablero
def colocar_barcos(barcos, tablero):
    for barco in barcos:
        for casilla in barco:
            tablero[casilla] = "O"
    return tablero


#5 funcion que comprueba si hay barcos solapados (casillas repetidas)
def hay_solape(flota): #esta parte se pega en la función crear flota
    ocupadas = []
    for barco in flota:
        for casilla in barco:
            if casilla in ocupadas:
                return True      # casilla repetida: hay solape
            ocupadas.append(casilla)
    return False 


#6 Función de disparar jugador 
def disparar(tablero_barcos_rival, tablero_disparos_jugador):
    try:
        fila = int(input("fila (0-9): "))
        columna = int(input("columna (0-9): "))
    except ValueError:
        print("Valor no válido, escribe números del 0 al 9")
        return False

    if fila < 0 or fila > 9 or columna < 0 or columna > 9:
        print("Fuera del tablero")
        return False

    if tablero_barcos_rival[fila, columna] == "O":
        tablero_barcos_rival[fila, columna] = "X"
        tablero_disparos_jugador[fila, columna] = "X"
        print("¡Tocado!")
        return True          # <- movido aquí: acierto
    else:
        tablero_disparos_jugador[fila, columna] = "A"
        print("Agua")
        return False         # <- movido aquí: fallo


#7 Función de disparar de la máquina (rival)
def disparar_rival(tablero_barcos_jugador, tablero_disparos_rival):
    fila = np.random.randint(10)
    columna = np.random.randint(10)

    while tablero_disparos_rival[fila, columna] != "_":
        fila = np.random.randint(10)
        columna = np.random.randint(10)

    print("La máquina dispara a:", fila, columna)

    if tablero_barcos_jugador[fila, columna] == "O":
        tablero_barcos_jugador[fila, columna] = "X"
        tablero_disparos_rival[fila, columna] = "X"
        print("¡Tocado!")
        return True
    else:
        tablero_disparos_rival[fila, columna] = "A"
        print("Agua")
        return False

#7b Función para pintar los tableros
def pintar(t_barcos_jugador, t_disparos_jugador):
    print("______TUS BARCOS______")
    print(t_barcos_jugador)
    print("______TUS DISPAROS______")
    print(t_disparos_jugador)

#8 Función de turnos
def turnos(t_barcos_rival, t_disparos_rival, t_barcos_jugador, t_disparos_jugador):
    turno_jugador = True  # empieza el jugador
    while True:
        if turno_jugador == True:
            print("turno jugador")
            pintar(t_barcos_jugador, t_disparos_jugador)
            acierto = disparar(t_barcos_rival, t_disparos_jugador)
            if (t_barcos_rival == "O").sum() == 0:
                print("¡HAS GANADO!")
                break
            if acierto == False:
                turno_jugador = False
        else:
            print("turno rival")
            acierto = disparar_rival(t_barcos_jugador, t_disparos_rival)
            if (t_barcos_jugador == "O").sum() == 0:
                print("HAS PERDIDO")
                break
            if acierto == False:
                turno_jugador = True
