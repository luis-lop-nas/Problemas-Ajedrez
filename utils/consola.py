def mostrar_movimientos_caballo(caballo, profundidad):
    total = caballo.movimientos_totales(profundidad)
    print(f"\n🐴 Movimientos válidos del caballo con {profundidad} movimiento(s): {total}")


def mostrar_solucion_reinas(tablero):
    if tablero.resolver():
        print(f"\n👑 Solución para {tablero.n} reinas:")
        for col, fila in enumerate(tablero.posiciones):
            print(f" - Columna {col}: Fila {fila}")
    else:
        print(f"\n❌ No hay solución para {tablero.n} reinas.")