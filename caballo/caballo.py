from .teclado import Teclado

class Caballo:
    def __init__(self, teclado=None):
        # Si no se pasa un teclado, se crea uno por defecto
        self.teclado = teclado if teclado else Teclado()

    def contar_movimientos(self, desde, profundidad):
        if profundidad == 0:
            return 1
        total = 0
        for siguiente in self.teclado.movimientos_validos(desde):
            total += self.contar_movimientos(siguiente, profundidad - 1)
        return total

    def movimientos_totales(self, profundidad):
        total = 0
        for i in range(10):
            total += self.contar_movimientos(i, profundidad)
        return total