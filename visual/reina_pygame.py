import pygame
from .colores import BLANCO, NEGRO, ROJO

TAM_CASILLA = 60  # tamaño en píxeles de cada casilla

def mostrar_tablero_reinas(tablero, cantidad_reinas):
    n = tablero.n
    ancho = alto = TAM_CASILLA * n

    pygame.init()
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption(f"Reinas en tablero {n}x{n}")
    reloj = pygame.time.Clock()

    # Cargar una reina como imagen (opcional), por ahora usamos círculo rojo
    running = True
    while running:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False

        # Dibujar tablero
        pantalla.fill(BLANCO)
        for fila in range(n):
            for col in range(n):
                color = BLANCO if (fila + col) % 2 == 0 else NEGRO
                rect = pygame.Rect(col * TAM_CASILLA, fila * TAM_CASILLA, TAM_CASILLA, TAM_CASILLA)
                pygame.draw.rect(pantalla, color, rect)

        # Dibujar reinas
        for col in range(cantidad_reinas):
            fila = tablero.posiciones[col]
            centro_x = col * TAM_CASILLA + TAM_CASILLA // 2
            centro_y = fila * TAM_CASILLA + TAM_CASILLA // 2
            pygame.draw.circle(pantalla, ROJO, (centro_x, centro_y), TAM_CASILLA // 3)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()