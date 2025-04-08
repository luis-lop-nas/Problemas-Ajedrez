import pygame
from .colores import obtener_colores

TAM_CASILLA = 60

class TableroReinasPygame:
    def __init__(self, tablero, cantidad_reinas):
        self.tablero = tablero
        self.cantidad_reinas = cantidad_reinas
        self.n = tablero.n
        self.ancho = TAM_CASILLA * self.n
        self.alto = TAM_CASILLA * self.n
        self.BL, self.NE, self.RO = obtener_colores()

        pygame.init()
        self.pantalla = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption(f"Reinas en tablero {self.n}x{self.n}")
        self.reloj = pygame.time.Clock()

    def dibujar_tablero(self):
        for fila in range(self.n):
            for col in range(self.n):
                color = self.BL if (fila + col) % 2 == 0 else self.NE
                rect = pygame.Rect(col * TAM_CASILLA, fila * TAM_CASILLA, TAM_CASILLA, TAM_CASILLA)
                pygame.draw.rect(self.pantalla, color, rect)

    def dibujar_reinas(self):
        # Cargar la imagen de la reina solo una vez
        if not hasattr(self, 'img_reina'):
            try:
                self.img_reina = pygame.image.load("visual/img/reina.png")
                self.img_reina = pygame.transform.scale(self.img_reina, (TAM_CASILLA, TAM_CASILLA))
            except Exception as e:
                print("⚠️ No se pudo cargar la imagen de la reina:", e)
                return

        # Dibujar la reina en cada posición
        for col in range(self.cantidad_reinas):
            fila = self.tablero.posiciones[col]
            x = col * TAM_CASILLA
            y = fila * TAM_CASILLA
            self.pantalla.blit(self.img_reina, (x, y))
            
    def mostrar(self):
        running = True
        while running:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    running = False

            self.pantalla.fill(self.BL)
            self.dibujar_tablero()
            self.dibujar_reinas()
            pygame.display.flip()
            self.reloj.tick(60)

        pygame.quit()