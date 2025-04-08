from caballo.caballo import Caballo
from reina.tablero import Tablero
from utils.consola import mostrar_movimientos_caballo, mostrar_solucion_reinas
from visual.reina_pygame import TableroReinasPygame

def main():
    print("=== PROBLEMAS DE AJEDREZ ===")

    # 🐴 Problema del Caballo
    profundidad = int(input("\n👉 Ingrese la cantidad de movimientos del caballo: "))
    caballo = Caballo()
    mostrar_movimientos_caballo(caballo, profundidad)

    # 👑 Problema de las N-Reinas
    cantidad_reinas = int(input("\n👉 Ingrese la cantidad de reinas: "))
    tam_tablero = int(input("📐 Ingrese el tamaño del tablero (n x n): "))

    if cantidad_reinas > tam_tablero:
        print("\n⚠️ Advertencia: No es posible colocar más reinas que columnas. No hay solución.")
        return
    tablero = Tablero(tam_tablero)
    mostrar_solucion_reinas(tablero, cantidad_reinas)
    
    # Mostrar visualización en Pygame
    visual = TableroReinasPygame(tablero, cantidad_reinas)
    visual.mostrar()