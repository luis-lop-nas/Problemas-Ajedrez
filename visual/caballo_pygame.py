import pygame
from .colores import obtener_colores

TAM_CASILLA = 80

# Mapeo de números a posiciones (x, y) en grilla de teclado
POSICIONES_TECLADO = {
    1: (0, 0), 2: (1, 0), 3: (2, 0),
    4: (0, 1), 5: (1, 1), 6: (2, 1),
    7: (0, 2), 8: (1, 2), 9: (2, 2),
    0: (1, 3)
}

class TecladoCaballoPygame:
    def __init__(self, caballo, profundidad):
        self.caballo = caballo
        self.profundidad = profundidad
        self.desde = 1  # Número desde el cual mostrar los destinos
        self.BL, self.NE, self.RO = obtener_colores()
        self.ancho = TAM_CASILLA * 3
        self.alto = TAM_CASILLA * 4 + 40  # espacio adicional para el texto

        pygame.init()
        pygame.font.init()

        self.pantalla = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption(f"Movimientos válidos del caballo con {profundidad} paso(s)")

        # Truco para que la ventana aparezca al frente en macOS
        pygame.display.set_mode((self.ancho + 1, self.alto + 1))
        pygame.display.set_mode((self.ancho, self.alto))

        self.fuente = pygame.font.Font(None, 40)
        assert self.fuente is not None, "⚠️ No se cargó la fuente correctamente"
        self.reloj = pygame.time.Clock()

    def dibujar_teclado(self, destinos=[]):
        for numero, (col, fila) in POSICIONES_TECLADO.items():
            x = col * TAM_CASILLA
            y = fila * TAM_CASILLA
            rect = pygame.Rect(x, y, TAM_CASILLA, TAM_CASILLA)

            if numero in destinos:
                pygame.draw.rect(self.pantalla, self.RO, rect)  # fondo rojo para destinos
            else:
                pygame.draw.rect(self.pantalla, self.NE, rect, width=2)

            texto = self.fuente.render(str(numero), True, self.NE)
            self.pantalla.blit(texto, (x + TAM_CASILLA // 3, y + TAM_CASILLA // 3))

    def mostrar(self):
        total = self.caballo.movimientos_totales(self.profundidad)
        destinos_validos = self.caballo.teclado.movimientos_validos(self.desde)

        running = True
        while running:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    running = False

            self.pantalla.fill(self.BL)
            self.dibujar_teclado(destinos_validos)

            # Fondo para el texto
            pygame.draw.rect(self.pantalla, self.BL, (0, TAM_CASILLA * 4, self.ancho, 40))
            texto = self.fuente.render(f"Total: {total}", True, self.RO)
            self.pantalla.blit(texto, (10, TAM_CASILLA * 4 + 5))

            pygame.display.flip()
            self.reloj.tick(60)

        pygame.quit()