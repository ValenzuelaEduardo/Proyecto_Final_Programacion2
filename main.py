import copy
import pygame
import math
import random
from board import boards  # Asegúrate de tener un módulo board con una matriz boards definida.

pygame.init()

WIDTH = 900
HEIGHT = 800
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

# Cargar y escalar sprites fuera de las clases
sprite_size = WIDTH // 20
animal_sprites = []

for i in range(1, 11):  # Asumiendo que tienes 10 imágenes nombradas animal1.png a animal10.png
    animal_image = pygame.image.load(f"animales_images/animal{i}.png")
    animal_image = pygame.transform.scale(animal_image, (sprite_size, sprite_size))
    animal_sprites.append(animal_image)

# Clase Organismo
class Organismo(pygame.sprite.Sprite):
    def __init__(self, columna, fila, ancho, alto, tamaño_celda):
        super().__init__()
        self.image = pygame.Surface([ancho, alto])
        self.columna = columna
        self.fila = fila
        self.tamaño_celda = tamaño_celda  # Almacenar tamaño_celda como atributo de instancia
        self.rect = self.image.get_rect(topleft=(columna * self.tamaño_celda, fila * self.tamaño_celda))
        self.vida = True
        self.energia = 100

    def update(self):
        pass

class Animal(Organismo):
    def __init__(self, columna, fila, ancho, alto, especie, dieta, sprite_index, columnas, filas, tamaño_celda):
        super().__init__(columna, fila, ancho, alto, tamaño_celda)
        self.especie = especie
        self.dieta = dieta
        self.contador_movimiento = 0
        self.tiempo_para_moverse = 60
        self.columnas = columnas
        self.filas = filas
        
        # Asignar el sprite correspondiente al animal
        if 0 <= sprite_index < len(animal_sprites):
            self.image = animal_sprites[sprite_index]
        else:
            raise IndexError("Sprite index fuera de rango")
        
    def mover(self):
        if self.contador_movimiento >= self.tiempo_para_moverse:
            direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            dx, dy = random.choice(direcciones)
            nueva_columna = self.columna + dx
            nueva_fila = self.fila + dy
            if 0 <= nueva_columna < self.columnas and 0 <= nueva_fila < self.filas:
                self.columna = nueva_columna
                self.fila = nueva_fila
                self.rect.topleft = (self.columna * self.tamaño_celda, self.fila * self.tamaño_celda)
            self.contador_movimiento = 0
        else:
            self.contador_movimiento += 1
    def dibujar(self, pantalla):
        pantalla.blit(self.image, self.rect)
    def update(self):
        self.mover()

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

# Definir tamaño_celda
tamaño_celda = sprite_size

# Inicializar la lista de instancias de animales
animal_instances = []

# Definir variables faltantes antes del bucle while
especie = "EspecieEjemplo"  # Valor de ejemplo para la especie
dieta = "Herbívoro"  # Valor de ejemplo para la dieta
columnas = len(level[0])  # Número de columnas basado en el nivel
filas = len(level)  # Número de filas basado en el nivel

while len(animal_instances) < 10:
    x = random.randint(0, columnas - 1)
    y = random.randint(0, filas - 1)
    if level[y][x] == 0 and all(animal.columna != x or animal.fila != y for animal in animal_instances):
        sprite_index = random.randint(0, len(animal_sprites) - 1)
        ancho = alto = tamaño_celda  # Suponiendo que el ancho y alto del sprite es igual al tamaño_celda
        animal = Animal(x, y, ancho, alto, especie, dieta, sprite_index, columnas, filas, tamaño_celda)
        animal_instances.append(animal)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('green')  # El fondo con color verde (debería ir antes de dibujar cualquier cosa más)
    draw_board()  # Dibujar el nivel antes de los animales

    # Actualizar y dibujar los animales
    for animal in animal_instances:
        animal.update()  # Llamada al método update en lugar de mover directamente
        animal.dibujar(screen)  # Llama al método dibujar implementado

    timer.tick(fps)
    if counter < 19:
        counter += 1
        if counter > 3:
            flicker = False
    else:
        counter = 0
        flicker = True

    pygame.display.flip()

    # Mantener el juego corriendo al FPS deseado
    timer.tick(fps)

pygame.quit()