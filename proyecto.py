import pygame
import random
import sys
from pygame.locals import QUIT

BROWN = (199, 66, 37)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Organismo(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vida = 100
        self.energia = 50
        self.velocidad = 2

    def mover(self):
        self.rect.x += random.randint(-self.velocidad, self.velocidad)
        self.rect.y += random.randint(-self.velocidad, self.velocidad)

    def reproducir(self):
        pass

    def morir(self):
        pass

class Animal(Organismo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill(RED)
        self.especie = "Especie"
        self.dieta = "Herbivoro"
        self.direccion = 1

    def cazar(self):
        pass

    def mover_derecha(self):
        self.rect.x += self.velocidad

    def mover_izquierda(self):
        self.rect.x -= self.velocidad

class Planta(Organismo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image.fill(GREEN)

    def fotosintesis(self):
        pass

    def reproducir_por_semillas(self):
        pass

class Ambiente(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def afectar_ecosistema(self):
        pass

def main():
    pygame.init()

    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Simulador de Ecosistemas")

    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    organismo = Organismo(100, 100)
    animal = Animal(200, 200)
    planta = Planta(300, 300)
    ambiente = Ambiente(400, 400)

    all_sprites.add(organismo, animal, planta, ambiente)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        all_sprites.update()

        for sprite in all_sprites:
            if isinstance(sprite, Animal):
                if sprite.rect.x > 600 or sprite.rect.x < 100:
                    sprite.direccion *= -1

                if sprite.direccion == 1:
                    sprite.mover_derecha()
                else:
                    sprite.mover_izquierda()

        screen.fill(BROWN)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
