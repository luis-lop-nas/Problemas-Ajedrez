def mostrar_movimientos_caballo(caballo, profundidad):
    total = caballo.movimientos_totales(profundidad)
    print(f"\n🐴 Movimientos válidos del caballo con {profundidad} movimiento(s): {total}")


def mostrar_solucion_reinas(tablero, cantidad_reinas):
    if tablero.resolver(cantidad_reinas):
        print(f"\n👑 Solución para colocar {cantidad_reinas} reinas en un tablero de {tablero.n}x{tablero.n}:")
        for col, fila in enumerate(tablero.posiciones[:cantidad_reinas]):
            print(f" - Reina en Columna {col}: Fila {fila}")
    else:
        print(f"\n❌ No se encontró solución para {cantidad_reinas} reinas en un tablero de {tablero.n}x{tablero.n}.")