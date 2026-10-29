import funciones as f

# 1. Crear los 4 tableros (matrices 10x10 de "_")
t_barcos_rival = f.crear_tablero()
t_disparos_rival = f.crear_tablero()
t_barcos_jugador = f.crear_tablero()
t_disparos_jugador = f.crear_tablero()

# 2. Crear las dos flotas (6 barcos cada una, dentro del tablero y sin solapes : 16 posiciones de 100)
flota_rival = f.crear_flota()
flota_jugador = f.crear_flota()

# 3. Colocar cada flota en su tablero de barcos
t_barcos_rival = f.colocar_barcos(flota_rival, t_barcos_rival)
t_barcos_jugador = f.colocar_barcos(flota_jugador, t_barcos_jugador)

# 4. Jugar: empieza el jugador y se alternan los turnos hasta que alguien gana
print("***** HUNDIR LA FLOTA *****")
f.turnos(t_barcos_rival, t_disparos_rival, t_barcos_jugador, t_disparos_jugador)