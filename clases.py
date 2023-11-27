import pygame
import random

class Organismo(pygame.sprite.Sprite):
    def __init__(self, columna, fila, ancho, alto, color):
        super().__init__()
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(color)
        self.columna = columna
        self.fila = fila
        self.rect = self.image.get_rect(topleft=(columna * tamaño_celda, fila * tamaño_celda))
        self.vida = True
        self.energia = 100

    def update(self):
        pass

class Planta(Organismo):
    def __init__(self, columna, fila, ancho, alto, color):
        super().__init__(columna, fila, ancho, alto, color)

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

todos_los_sprites = pygame.sprite.Group()
animales = pygame.sprite.Group()
plantas = pygame.sprite.Group()
