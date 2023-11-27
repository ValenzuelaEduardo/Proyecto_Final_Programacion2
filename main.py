import copy
from board import boards  # Asegúrate de tener un módulo board con una matriz boards definida.
import pygame
import math

pygame.init()

WIDTH = 900
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 30
font = pygame.font.Font('freesansbold.ttf', 20)
level = copy.deepcopy(boards)
color = 'blue'
PI = math.pi
counter = 0
flicker = False

# Carga de sprites para cada tipo de terreno
sprite0 = pygame.image.load("pasto.png")  # Asumiendo que tienes una imagen para el pasto
sprite1 = pygame.image.load("agua.jpg")   # Imagen para el agua
sprite2 = pygame.image.load("arbusto.png")  # Imagen para el arbusto
sprite3 = pygame.image.load("agujero.png")  # Imagen para el agujero

# Escalar sprites al tamaño del cuadrado si es necesario
sprite_size = WIDTH // 20
sprite0 = pygame.transform.scale(sprite0, (sprite_size, sprite_size))
sprite1 = pygame.transform.scale(sprite1, (sprite_size, sprite_size))
sprite2 = pygame.transform.scale(sprite2, (sprite_size, sprite_size))
sprite3 = pygame.transform.scale(sprite3, (sprite_size, sprite_size))

def draw_board():
    for i in range(len(level)):
        for j in range(len(level[i])):
            rect = pygame.Rect(j * sprite_size, i * sprite_size, sprite_size, sprite_size)
            if level[i][j] == 0:
                screen.blit(sprite0, rect)
            elif level[i][j] == 1:
                screen.blit(sprite1, rect)
            elif level[i][j] == 2:
                screen.blit(sprite2, rect)
            elif level[i][j] == 3:
                screen.blit(sprite3, rect)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    timer.tick(fps)
    if counter < 19:
        counter += 1
        if counter > 3:
            flicker = False
    else:
        counter = 0
        flicker = True

    screen.fill('green')  # El fondo con color verde (podrías usar un sprite de pasto también)
    draw_board()

    pygame.display.flip()

pygame.quit()
