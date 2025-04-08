class Teclado:
    def __init__(self):
        # Diccionario con las posibles jugadas del caballo desde cada número
        self.movimientos = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

    def movimientos_validos(self, desde):
        return self.movimientos.get(desde, [])