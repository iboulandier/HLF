import numpy as np

#1 funcion que crea tableros de 10x10. 
def crear_tablero(tamaño=10):
    tablero = np.full((tamaño, tamaño), "_") #crea una tupla de 10x10
    return tablero


#2 funcion crear barcos (con posición inicial aleatoria, crear con if que queden dentro de rango/tablero, en crear flota comprobaré que no se solapen)
def crear_barco(eslora):
    barco = []
    pos_ini = (np.random.randint(10), np.random.randint(10))#creo la posición inicial de un barco al azar (del 0 al 9)
    p = 1 #contador que dice cuántas casillas me alejo de la pos_ini
    barco.append(pos_ini) #añade pos_ini al final de la lista de barco
    dir = np.random.choice(("v", "h"))

    if dir == "v": #en el caso de que sea vertical, haces este bucle
        for pos in np.arange(eslora -1): # haz un bucle que itere por el nº de veces que tiene la eslora -1 (porque ya tenemos la posición incial)
            barco.append((pos_ini[0] + p, pos_ini[1])) # añadele a la variable barco, las posiciones que faltan por determinar, y al ser vertical, varían las filas y las columnas se quedan estáticasg (dentro de la tupla, la primera posición (filas), es la posición 0, entonces sumale +1
            p = p + 1 # El bucle for repite su bloque. Al llegar al final del bloque, Python vuelve al for, y si quedan vueltas, ejecuta otra vez las mismas líneas de dentro. Por eso el orden dentro del bloque importa: append va primero (usa p tal como está) y p = p + 1 va después (lo prepara para la vuelta siguiente).
    else:
        for pos in np.arange(eslora -1):
            barco.append((pos_ini [0], pos_ini[1] + p))
            p = p + 1 #El bucle for repite su bloque. Al llegar al final del bloque, Python vuelve al for, y si quedan vueltas, ejecuta otra vez las mismas líneas de dentro. Por eso el orden dentro del bloque importa: append va primero (usa p tal como está) y p = p + 1 va después (lo prepara para la vuelta siguiente).
    return barco

#3 Función crear flota
def crear_flota():
    esloras_flota = [4, 3, 3, 2, 2, 2]
    flota = []
    for eslora in esloras_flota:  
        flota.append(crear_barco(eslora)) # Haz un bucle y transite-itera por cada elemento de esloras_flota, recoge ese número en eslora, y úsalo con crear_barco para fabricar un barco y añadirlo a la lista flota.

    for barco in flota: #haz un bucle y transita-itera por cada una de las sublistas que hay en la lista flota (en realidad esas sublistas son barcos) y llévatela a la variable barco
        for coor in barco: # haz un bucle y transita-itera por cada una de las tuplas que hay en un barco, y llevatelo a la variable coor
            for i in coor: #haz un bucle y transita-itera por cada fila y columna, para verificar que no sea menor que 0 o mayor que 9, porque estarían fuera de rango-tablero
                if i < 0 or i > 9:
                    print("generando flota de nuevo (fuera del tablero)")
                    return crear_flota() # si alguna fila o columna se sale de rango, empieza de nuevo a crear flota, en caso contrario: continua...

    if hay_solape(flota): #segunda condición. Si hay solape (para ello consulta la funcion hay solape, entonces imprime generando flota de nuevo, )
        print("generando flota de nuevo (solapados)")
        return crear_flota()

    return flota # si todas las variables se cumplen ( ni fuera de rango ni solape, crea la lista de listas con tuplas de  la que se compen la variable flota)


#4 funcion que comprueba si hay barcos solapados (casillas repetidas)
def hay_solape(flota): #esta parte se pega en la función crear flota. "hay_solape" recibe una flota previamente creada de manera aleatoria mediante bucles. (lista de barcos, cada barco lista de tuplas).
    ocupadas = [] #Crea una lista vacía ocupadas.
    for barco in flota:
        for casilla in barco:
            if casilla in ocupadas:
                return True      # casilla repetida: hay solape
            ocupadas.append(casilla) #estaparte del codigo append está fuera del if.
    return False 

#5 funcion que coloca los barcos en el tablero
def colocar_barcos(barcos, tablero):
    for barco in barcos:
        for casilla in barco:
            tablero[casilla] = "O" #casilla es una tupla (fila, columna), y NumPy acepta una tupla directamente entre corchetes. Es lo mismo que escribir tablero[2, 5] = "O". Por eso funciona sin tener que separar fila y columna.
    return tablero


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

    if tablero_barcos_rival[fila, columna] == "O"
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
