from caballo.caballo import Caballo
from reina.tablero import Tablero
from utils.consola import mostrar_movimientos_caballo, mostrar_solucion_reinas

def main():
    print("=== PROBLEMAS DE AJEDREZ ===")

    # 🐴 Problema del Caballo
    profundidad = int(input("\n👉 Ingrese la cantidad de movimientos del caballo: "))
    caballo = Caballo()
    mostrar_movimientos_caballo(caballo, profundidad)

    # 👑 Problema de las N-Reinas
    n = int(input("\n👉 Ingrese el número de reinas (y tamaño del tablero): "))
    tablero = Tablero(n)
    mostrar_solucion_reinas(tablero)