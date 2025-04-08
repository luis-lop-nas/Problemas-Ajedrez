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
        self.BL, self.NE, self.RO = obtener_colores()
        self.ancho = TAM_CASILLA * 3
        self.alto = TAM_CASILLA * 4 + 40 # espacio para el texto

        pygame.init()
        self.pantalla = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption(f"Movimientos válidos del caballo con {profundidad} paso(s)")
        self.fuente = pygame.font.SysFont(None, 40)
        self.reloj = pygame.time.Clock()

    def dibujar_teclado(self):
        for numero, (col, fila) in POSICIONES_TECLADO.items():
            x = col * TAM_CASILLA
            y = fila * TAM_CASILLA
            rect = pygame.Rect(x, y, TAM_CASILLA, TAM_CASILLA)
            pygame.draw.rect(self.pantalla, self.NE, rect, width=2)
            texto = self.fuente.render(str(numero), True, self.NE)
            self.pantalla.blit(texto, (x + TAM_CASILLA // 3, y + TAM_CASILLA // 3))

    def mostrar(self):
        total = self.caballo.movimientos_totales(self.profundidad)
        running = True
        while running:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    running = False

            self.pantalla.fill(self.BL)
            self.dibujar_teclado()

            # Mostrar el total en pantalla
            texto = self.fuente.render(f"Total: {total}", True, self.RO)
            self.pantalla.blit(texto, (10, self.alto + 10))  # fuera del área del teclado

            pygame.display.flip()
            self.reloj.tick(60)

        pygame.quit()