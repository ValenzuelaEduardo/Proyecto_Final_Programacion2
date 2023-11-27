import pygame
import random
from clases import * 

pygame.init()
pantalla_ancho = 907
pantalla_alto = 800
tamaño_celda = 30
columnas = pantalla_ancho / tamaño_celda
filas = pantalla_alto / tamaño_celda

pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_alto))
pygame.display.set_caption("Simulación de Ecosistema en Cuadrícula")

# Cargamos y escalamos la imagen de fondo
imagen_fondo = pygame.image.load('mapa.jpg')
imagen_fondo = pygame.transform.scale(imagen_fondo, (pantalla_ancho, pantalla_alto))

FPS = 80

for _ in range(10):
    planta = Planta(random.randint(0, columnas-1), random.randint(0, filas-1), tamaño_celda, tamaño_celda, (0, 255, 0))
    animal = Animal(random.randint(0, columnas-1), random.randint(0, filas-1), tamaño_celda, tamaño_celda, (255, 0, 0), "Especie", "Carnívoro")
    plantas.add(planta)
    animales.add(animal)
    todos_los_sprites.add(planta)
    todos_los_sprites.add(animal)

corriendo = True
reloj = pygame.time.Clock()
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Bliteamos la imagen de fondo en la pantalla
    pantalla.blit(imagen_fondo, (0, 0))

    todos_los_sprites.update()

    for entidad in todos_los_sprites:
        pantalla.blit(entidad.image, entidad.rect)

    pygame.display.flip()
    reloj.tick(FPS)

pygame.quit()