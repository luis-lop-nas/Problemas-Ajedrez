class Tablero:
    def __init__(self, n):
        self.n = n
        self.posiciones = [-1] * n  # Cada índice representa una columna, y el valor la fila

    def es_valido(self, col, fila):
        for c in range(col):
            if self.posiciones[c] == fila:
                return False  # misma fila
            if abs(self.posiciones[c] - fila) == abs(c - col):
                return False  # misma diagonal
        return True

    def resolver(self, col=0):
        if col == self.n:
            return True  # Solución completa
        for fila in range(self.n):
            if self.es_valido(col, fila):
                self.posiciones[col] = fila
                if self.resolver(col + 1):
                    return True
        return False