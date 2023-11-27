import copy
from board import boards  # Asegúrate de tener un módulo board con una matriz boards definida.
import pygame
import math
from clases import *  # Asegúrate de que las clases necesarias estén definidas aquí
import random

pygame.init()

# Configuración de la pantalla
pantalla_ancho = 900
pantalla_alto = 900
tamaño_celda = 30

# Asegurándonos de que las columnas y filas sean enteros
columnas = pantalla_ancho // tamaño_celda
filas = pantalla_alto // tamaño_celda

screen = pygame.display.set_mode([pantalla_ancho, pantalla_alto])
timer = pygame.time.Clock()

fps = 30

font = pygame.font.Font('freesansbold.ttf', 20)
level = copy.deepcopy(boards)
color = 'blue'
PI = math.pi
counter = 0
flicker = False

# Carga de sprites
sprite0 = pygame.image.load("pasto.png")
sprite1 = pygame.image.load("agua.jpg")
sprite2 = pygame.image.load("arbusto.png")
sprite3 = pygame.image.load("agujero.png")

sprite_size = pantalla_ancho // 20

# Escalado de sprites
sprite0 = pygame.transform.scale(sprite0, (sprite_size, sprite_size))
sprite1 = pygame.transform.scale(sprite1, (sprite_size, sprite_size))
sprite2 = pygame.transform.scale(sprite2, (sprite_size, sprite_size))
sprite3 = pygame.transform.scale(sprite3, (sprite_size, sprite_size))

pygame.display.set_caption("Simulación de Ecosistema en Cuadrícula")

# Inicialización de grupos de sprites
plantas = pygame.sprite.Group()
animales = pygame.sprite.Group()
todos_los_sprites = pygame.sprite.Group()

# Creación y adición de plantas y animales a los grupos de sprites
for _ in range(10):
    planta = Planta(random.randint(0, columnas-1), random.randint(0, filas-1), tamaño_celda, tamaño_celda, (0, 255, 0))
    animal = Animal(random.randint(0, columnas-1), random.randint(0, filas-1), tamaño_celda, tamaño_celda, (255, 0, 0), "Especie", "Carnívoro")
    plantas.add(planta)
    animales.add(animal)
    todos_los_sprites.add(planta)
    todos_los_sprites.add(animal)

# Función para dibujar el tablero (debes definirla)
def draw_board():
    for y in range(filas):
        for x in range(columnas):
            rect = pygame.Rect(x*tamaño_celda, y*tamaño_celda, tamaño_celda, tamaño_celda)
            if level[y][x] == 0:
                screen.blit(sprite0, rect)
            elif level[y][x] == 1:
                screen.blit(sprite1, rect)
            elif level[y][x] == 2:
                screen.blit(sprite2, rect)
            elif level[y][x] == 3:
                screen.blit(sprite3, rect)

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualización de estados
    todos_los_sprites.update()

    # Limpieza de la pantalla
    screen.fill((0, 0, 0))

    # Dibujo del tablero
    draw_board()

    # Dibujo de todos los sprites
    todos_los_sprites.draw(screen)

    # Actualizar pantalla
    pygame.display.flip()

    # Controlar el bucle con el reloj
    timer.tick(fps)

pygame.quit()
