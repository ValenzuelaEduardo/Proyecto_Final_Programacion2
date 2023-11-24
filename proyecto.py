import pygame
import sys
from pygame.locals import QUIT

BROWN = (199, 66, 37)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CELESTE = (173, 216, 230)

CELL_SIZE = 20
MAP_WIDTH = 40
MAP_HEIGHT = 30

def create_empty_map():
    return [[None for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]

def spawn_organism(mapa, x, y, tipo, color):
    mapa[y][x] = (tipo, color)

def spawn_animal(mapa, x, y, especie):
    color = RED  # Puedes ajustar el color según la especie si es necesario
    spawn_organism(mapa, x, y, "animal", color)

def main():
    pygame.init()

    width, height = CELL_SIZE * MAP_WIDTH, CELL_SIZE * MAP_HEIGHT
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Simulador de Ecosistemas")

    clock = pygame.time.Clock()

    tiempo_inicial = pygame.time.get_ticks()

    mapa = create_empty_map()

    # Agregar algunos animales al mapa
    spawn_animal(mapa, 5, 5, "león")
    spawn_animal(mapa, 10, 10, "cebra")
    spawn_animal(mapa, 20, 15, "león")
    spawn_animal(mapa, 30, 25, "cebra")

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        tiempo_transcurrido = pygame.time.get_ticks() - tiempo_inicial

        # Cambiar a color celeste cada 30 segundos (30000 milisegundos)
        if tiempo_transcurrido % 30000 < 15000:
            screen.fill(CELESTE)
        else:
            screen.fill(BROWN)

        # Dibujar el mapa
        for y, row in enumerate(mapa):
            for x, organismo in enumerate(row):
                if organismo:
                    pygame.draw.rect(screen, organismo[1], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
