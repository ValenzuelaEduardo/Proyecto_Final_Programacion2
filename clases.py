import random
import pygame

class Organismo(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto, color):
        super().__init__()
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.vida = True
        self.energia = 100
        self.velocidad = random.randint(1, 5)

    def mover(self, limites_pantalla):
        direcciones = [-1, 0, 1]
        dx = random.choice(direcciones) * self.velocidad
        dy = random.choice(direcciones) * self.velocidad

        if self.rect.left + dx < 0 or self.rect.right + dx > limites_pantalla[0]:
            dx = -dx
        if self.rect.top + dy < 0 or self.rect.bottom + dy > limites_pantalla[1]:
            dy = -dy

        self.rect.x += dx
        self.rect.y += dy

    def update(self):
        self.mover((pantalla_ancho, pantalla_alto))

class Animal(Organismo):
    def __init__(self, x, y, ancho, alto, color, especie, dieta):
        super().__init__(x, y, ancho, alto, color)
        self.especie = especie
        self.dieta = dieta

class Planta(Organismo):
    def __init__(self, x, y, ancho, alto, color):
        super().__init__(x, y, ancho, alto, color)
        self.velocidad = 0
