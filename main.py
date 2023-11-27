import copy
from board import boards  # Asegúrate de tener un módulo board con una matriz boards definida.
import pygame
import math
import random

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
animal_sprites = []

# Carga de sprites para cada tipo de terreno
sprite0 = pygame.image.load("pasto.png")  # Asumiendo que tienes una imagen para el pasto
sprite1 = pygame.image.load("planta.png")   # Imagen para el agua
sprite2 = pygame.image.load("Arbusto.png")  # Imagen para el arbusto
sprite3 = pygame.image.load("assets/map_images/AguaSupL.png")  # Imagen para el agujero
sprite4 = pygame.image.load("assets/map_images/AguaSup.png") # Imagen para la planta1
sprite5 = pygame.image.load("assets/map_images/AguaSupR.png")
sprite6 = pygame.image.load("assets/map_images/AguaL.png")
sprite7 = pygame.image.load("assets/map_images/Agua.png")
sprite8 = pygame.image.load("assets/map_images/AguaR.png")
sprite9 = pygame.image.load("assets/map_images/AguaAbajoL.png")
sprite10 = pygame.image.load("assets/map_images/AguaAbajo.png")
sprite11 = pygame.image.load("assets/map_images/AguaAbajoR.png")
sprite12 = pygame.image.load("planta1.png")


# Escalar sprites al tamaño del cuadrado si es necesario
sprite_size = WIDTH // 20
sprite0 = pygame.transform.scale(sprite0, (sprite_size, sprite_size))
sprite1 = pygame.transform.scale(sprite1, (sprite_size, sprite_size))
sprite2 = pygame.transform.scale(sprite2, (sprite_size, sprite_size))
sprite3 = pygame.transform.scale(sprite3, (sprite_size, sprite_size))
sprite4 = pygame.transform.scale(sprite4, (sprite_size, sprite_size))
sprite5 = pygame.transform.scale(sprite5, (sprite_size, sprite_size))
sprite6 = pygame.transform.scale(sprite6, (sprite_size, sprite_size))
sprite7 = pygame.transform.scale(sprite7, (sprite_size, sprite_size))
sprite8 = pygame.transform.scale(sprite8, (sprite_size, sprite_size))
sprite9 = pygame.transform.scale(sprite9, (sprite_size, sprite_size))
sprite10 = pygame.transform.scale(sprite10, (sprite_size, sprite_size))
sprite11 = pygame.transform.scale(sprite11, (sprite_size, sprite_size))
sprite12 = pygame.transform.scale(sprite12, (sprite_size, sprite_size))

for i in range(1, 11):  # Asumiendo que tienes 10 imágenes nombradas animal1.png, animal2.png, ..., animal10.png
    animal_image = pygame.image.load(f"animales_images/animal{i}.png")
    animal_image = pygame.transform.scale(animal_image, (sprite_size, sprite_size))  # Asumiendo que quieres que los animales tengan el mismo tamaño que un cuadro del tablero
    animal_sprites.append(animal_image)

animal_positions_sprites = []

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
            elif level[i][j] == 4:
                screen.blit(sprite4, rect)
            elif level[i][j] == 5:
                screen.blit(sprite5, rect)
            elif level[i][j] == 6:
                screen.blit(sprite6, rect)
            elif level[i][j] == 7:
                screen.blit(sprite7, rect)
            elif level[i][j] == 8:
                screen.blit(sprite8, rect)
            elif level[i][j] == 9:
                screen.blit(sprite9, rect)
            elif level[i][j] == 10:
                screen.blit(sprite10, rect)
            elif level[i][j] == 11:
                screen.blit(sprite11, rect)
            elif level[i][j] == 12:
                screen.blit(sprite12, rect)
                
while len(animal_positions_sprites) < 10:  # Quieres 10 animales
    x = random.randint(0, 19)  # Columna aleatoria
    y = random.randint(0, 19)  # Fila aleatoria

    # Comprobar si la posición está en pasto y no está ya ocupada por otro animal
    if level[y][x] == 0 and (x, y) not in [pos for pos, spr in animal_positions_sprites]:
        animal_sprite = random.choice(animal_sprites)  # Elige un sprite de animal al azar
        animal_positions_sprites.append(((x, y), animal_sprite))

def draw_animals():
    for pos, sprite in animal_positions_sprites:
        pos_x = pos[0] * sprite_size
        pos_y = pos[1] * sprite_size
        screen.blit(sprite, (pos_x, pos_y))


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
    draw_animals()
    pygame.display.flip()

pygame.quit()
