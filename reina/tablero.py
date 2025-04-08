class Tablero:
    def __init__(self, n):
        self.n = n  # tamaño del tablero (n x n)
        self.posiciones = [-1] * n  # índice = columna, valor = fila

    def es_valido(self, col, fila):
        for c in range(col):
            if self.posiciones[c] == fila:
                return False  # misma fila
            if abs(self.posiciones[c] - fila) == abs(c - col):
                return False  # misma diagonal
        return True

    def resolver(self, cantidad_reinas, col=0):
        if col == cantidad_reinas:
            return True  # colocó todas las reinas necesarias
        for fila in range(self.n):
            if self.es_valido(col, fila):
                self.posiciones[col] = fila
                if self.resolver(cantidad_reinas, col + 1):
                    return True
        return False