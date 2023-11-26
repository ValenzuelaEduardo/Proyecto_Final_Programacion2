# Clase Organismo
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

# Subclase Planta
class Planta(Organismo):
    def __init__(self, columna, fila, ancho, alto, color):
        super().__init__(columna, fila, ancho, alto, color)

    def update(self):
        pass

# Subclase Animal
class Animal(Organismo):
    def __init__(self, columna, fila, ancho, alto, color, especie, dieta):
        super().__init__(columna, fila, ancho, alto, color)
        self.especie = especie
        self.dieta = dieta
        self.contador_movimiento = 0
        self.tiempo_para_moverse = 60  # Ajusta este valor para cambiar la velocidad

    def mover(self):
        if self.contador_movimiento >= self.tiempo_para_moverse:
            direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # izquierda, derecha, arriba, abajo
            dx, dy = random.choice(direcciones)
            nueva_columna = self.columna + dx
            nueva_fila = self.fila + dy
            if 0 <= nueva_columna < columnas and 0 <= nueva_fila < filas:
                self.columna = nueva_columna
                self.fila = nueva_fila
                self.rect.topleft = (self.columna * tamaño_celda, self.fila * tamaño_celda)
            self.contador_movimiento = 0

    def update(self):
        self.contador_movimiento += 1
        self.mover()
