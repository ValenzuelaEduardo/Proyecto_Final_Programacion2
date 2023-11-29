import pygame
import random
import sys

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO = 800
ALTO = 800

# Tamaño del cuadrado (celda)
TAMANO_CELDA = 40

# Cargar y escalar imágenes
IMAGENES = {
    0: pygame.image.load('assets/map_images/pasto.png'),   # Pasto
    1: pygame.image.load('assets/map_images/planta.png'),    # Agujero
    3: pygame.image.load('assets/map_images/AguaSupL.png'), 
    4: pygame.image.load('assets/map_images/AguaSup.png'), 
    5: pygame.image.load('assets/map_images/AguaSupR.png'), 
    6: pygame.image.load('assets/map_images/AguaL.png'), 
    7: pygame.image.load('assets/map_images/Agua.png'), 
    8: pygame.image.load('assets/map_images/AguaR.png'), 
    9: pygame.image.load('assets/map_images/AguaAbajoL.png'), 
    10: pygame.image.load('assets/map_images/AguaAbajo.png'), 
    11: pygame.image.load('assets/map_images/AguaAbajoR.png'), 
}

for key, image in IMAGENES.items():
    IMAGENES[key] = pygame.transform.scale(image, (TAMANO_CELDA, TAMANO_CELDA))

SPRITE_PLANTAS = {
    pygame.image.load('assets/map_images/planta.png'),
    pygame.image.load('assets/map_images/arbusto.png'),      
    pygame.image.load('assets/map_images/planta1.png'),         
}


SPRITE_PLANTAS_NOCHE={
    1: pygame.image.load('assets/noche/planta.png'),    
    2: pygame.image.load('assets/noche/arbusto.png'), 
    12: pygame.image.load('assets/noche/planta1.png')
}
# Cargar y escalar imágenes
IMAGENES_NOCHE = {
    0: pygame.image.load('assets/noche/pasto.png'),   # Pasto

    3: pygame.image.load('assets/noche/AguaSupL.png'), 
    4: pygame.image.load('assets/noche/AguaSup.png'), 
    5: pygame.image.load('assets/noche/AguaSupR.png'), 
    6: pygame.image.load('assets/noche/AguaL.png'), 
    7: pygame.image.load('assets/noche/Agua.png'), 
    8: pygame.image.load('assets/noche/AguaR.png'), 
    9: pygame.image.load('assets/noche/AguaAbajoL.png'), 
    10: pygame.image.load('assets/noche/AguaAbajo.png'), 
    11: pygame.image.load('assets/noche/AguaAbajoR.png'), 
}



for key, image in IMAGENES_NOCHE.items():
    IMAGENES_NOCHE[key] = pygame.transform.scale(image, (TAMANO_CELDA, TAMANO_CELDA))

    
SPRITES_ANIMALES_DEPREDADOR = {
    'depredador1': pygame.image.load('assets/depredador/depredador1.png'),
    'depredador2': pygame.image.load('assets/depredador/depredador2.png'),
    'depredador3': pygame.image.load('assets/depredador/depredador3.png'),
    'depredador4': pygame.image.load('assets/depredador/depredador4.png'),
}

SPRITES_ANIMALES_PRESA={
    # ... Añade el resto de los sprites de depredadores
    'normal1': pygame.image.load('assets/presas/normal1.png'),
    'normal2': pygame.image.load('assets/presas/normal2.png'),
    'normal3': pygame.image.load('assets/presas/normal3.png'),
    'normal4': pygame.image.load('assets/presas/normal4.png'),
    'normal5': pygame.image.load('assets/presas/normal5.png'),
    'normal6': pygame.image.load('assets/presas/normal6.png'),
    # ... Añade el resto de los sprites normales
}

for key, image in SPRITES_ANIMALES_DEPREDADOR.items():
    SPRITES_ANIMALES_DEPREDADOR[key] = pygame.transform.scale(image, (TAMANO_CELDA, TAMANO_CELDA))



# Crear la ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
boards = [
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # Fila 1
    [0,  0,  0,  0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4], # Fila 2
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #3
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #4
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #5
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#6
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#7
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#8
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#9
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#10
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#11
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#12
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#13
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#14
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#15
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#16
    [0,  3,  4,  4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#17
    [0,  6,  7,  7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#18
    [0,  9,  10, 10, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4], # Fila 19
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Fila 20
]
# Asignamos la matriz a una variable para facilitar su uso
matriz = boards
# Clases del ecosistema

class Organismo:
    def __init__(self, posicion, vida, energia, velocidad):
        self.posicion = posicion
        self.vida = vida
        self.energia = energia
        self.velocidad = velocidad

def direccion_aleatoria(rango_movimiento):
    dx = random.randint(-rango_movimiento, rango_movimiento)
    dy = random.randint(-rango_movimiento, rango_movimiento)
    return dx, dy

class Animal(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad)
        self.especie = especie
        self.dieta = dieta
        self.sprite = SPRITES_ANIMALES_DEPREDADOR.get(especie, None)
        self.ultimo_movimiento = 0

    def cazar(self):
        pass

    def dibujar(self, pantalla):
        if self.sprite:
            pantalla.blit(self.sprite, (self.posicion[0] * TAMANO_CELDA, self.posicion[1] * TAMANO_CELDA))
        else:
            pygame.draw.rect(pantalla, (255, 0, 0),
                             (self.posicion[0] * TAMANO_CELDA, self.posicion[1] * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))

class Depredador(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta, presa):
        super().__init__(posicion, vida, energia, velocidad, especie, dieta)
        self.presa = presa

    def cazar(self, presas, matriz):
        # Comprobar si hay presas cerca
        for presa in presas:
            if abs(self.posicion[0] - presa.posicion[0]) <= 1 and abs(self.posicion[1] - presa.posicion[1]) <= 1:
                # Moverse una casilla extra hacia la presa
                dx = presa.posicion[0] - self.posicion[0]
                dy = presa.posicion[1] - self.posicion[1]
                self.mover(matriz, dx, dy)
                # Comer la presa si está en la misma posición
                if self.posicion == presa.posicion:
                    self.vida += random.choice([1, 2])  # Gana 1 o 2 de vida
                    presas.remove(presa)  # Remueve la presa de la lista

    def mover(self, matriz, dx=None, dy=None):
        tiempo_transcurrido = pygame.time.get_ticks()
        if tiempo_transcurrido - self.ultimo_movimiento >= 1500:
            if dx is None or dy is None:
                dx, dy = direccion_aleatoria(2)
            nuevo_x = self.posicion[0] + dx
            nuevo_y = self.posicion[1] + dy

            if 0 <= nuevo_x < len(matriz[0]) and 0 <= nuevo_y < len(matriz) and matriz[nuevo_y][nuevo_x] == 0:
                self.posicion = (nuevo_x, nuevo_y)
                self.ultimo_movimiento = tiempo_transcurrido

    def dibujar(self, pantalla):
        if self.sprite:
            pantalla.blit(self.sprite, (self.posicion[0] * TAMANO_CELDA, self.posicion[1] * TAMANO_CELDA))
        else:
            pygame.draw.rect(pantalla, (255, 0, 0),
                             (self.posicion[0] * TAMANO_CELDA, self.posicion[1] * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))

def posicion_aleatoria_valida(matriz, valores_validos):
    while True:
        x = random.randint(0, len(matriz[0]) - 1)
        y = random.randint(0, len(matriz) - 1)
        if matriz[y][x] in valores_validos:
            return x, y

class Presa(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad, especie, dieta)

    def huir(self, depredadores, matriz):
        # Comprobar si hay depredadores cerca
        for depredador in depredadores:
            if abs(self.posicion[0] - depredador.posicion[0]) <= 1 and abs(self.posicion[1] - depredador.posicion[1]) <= 1:
                # Moverse en dirección opuesta al depredador
                dx = -(depredador.posicion[0] - self.posicion[0])
                dy = -(depredador.posicion[1] - self.posicion[1])
                self.mover(matriz, dx, dy)

    def mover(self, matriz, dx=None, dy=None):
        tiempo_transcurrido = pygame.time.get_ticks()
        if tiempo_transcurrido - self.ultimo_movimiento >= 2000:
            if dx is None or dy is None:
                dx, dy = direccion_aleatoria(1)
            nuevo_x = self.posicion[0] + dx
            nuevo_y = self.posicion[1] + dy

            if 0 <= nuevo_x < len(matriz[0]) and 0 <= nuevo_y < len(matriz) and matriz[nuevo_y][nuevo_x] == 0:
                self.posicion = (nuevo_x, nuevo_y)
                self.ultimo_movimiento = tiempo_transcurrido

    def dibujar(self, pantalla):
        if self.sprite:
            pantalla.blit(self.sprite, (self.posicion[0] * TAMANO_CELDA, self.posicion[1] * TAMANO_CELDA))
        else:
            pygame.draw.rect(pantalla, (255, 0, 0),
                             (self.posicion[0] * TAMANO_CELDA, self.posicion[1] * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))
            
    # Puedes agregar métodos específicos de las presas si es necesario

# Ejemplo de uso
# presa1 = Presa((0, 0), 50, 30, 4, "Cebra", "Herbívoro")

valores_cesped_arbustos = [0, 2]

lista_animales = []
for i in range(6):
    # Añadir animales en posiciones aleatorias donde haya pasto o arbustos
    lista_animales.append(Animal(
        posicion_aleatoria_valida(matriz, valores_cesped_arbustos),
        100,             # vida
        50,              # energía
        5,               # velocidad
        f'normal{i+1}',  # especie
        'DietaEjemplo'   # Proporciona una dieta válida
    ))

for i in range(4):
    # Añadir depredadores en posiciones aleatorias donde haya pasto o arbustos
    lista_animales.append(Depredador(
        posicion_aleatoria_valida(matriz, valores_cesped_arbustos),
        100,             # vida
        50,              # energía
        5,               # velocidad
        f'depredador{i+1}',    # especie
        'DietaEjemplo',  # Proporciona una dieta válida
        'PresaEjemplo'   # Proporciona una presa válida
    ))

class Planta(Organismo):
    def __init__(self, posicion, vida, energia):
        super().__init__(posicion, vida, energia, velocidad=0)  # Las plantas no se mueven
        self.tipo = 'planta'
        self.sprite = SPRITE_PLANTAS.get(f'{vida}{energia}', None)

    def fotosintesis(self):
        # Asumimos que la fotosíntesis siempre es exitosa por simplicidad
        self.vida += 1  # La planta gana 1 de vida
        self.energia += 1  # También podría ganar energía si así lo deseas

    def dibujar_pl(self, pantalla):
        if self.sprite:
            # Dibuja el sprite en la posición correspondiente
            pantalla.blit(self.sprite, (self.posicion[0] * TAMANO_CELDA, self.posicion[1] * TAMANO_CELDA))
        else:
            # Si no hay sprite, podrías dibujar un rectángulo o círculo como placeholder
            pygame.draw.rect(pantalla, (20, 255, 0), (self.posicion[0] * TAMANO_CELDA, self.posicion[1] * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))

    def reproducirse(self):
        # Puedes agregar la lógica de reproducción aquí
        pass

posiciones_de_plantas = []

plantas = [Planta((x, y), vida=5, energia=10) for x, y in posiciones_de_plantas]

# Después de cada ciclo en el juego, podrías llamar a la fotosíntesis para cada planta
for planta in plantas:
    planta.fotosintesis()
class Ambiente:
    def __init__(self):
        self.factores = []  # Lista de factores abióticos

    def cambiar_clima(self):
        # Lógica para cambiar el clima
        pass

    def dibujar_tablero(self, pantalla):
        for y, fila in enumerate(matriz):
            for x, valor in enumerate(fila):
                imagen = IMAGENES.get(valor)
                if imagen:
                    pantalla.blit(imagen, (x * TAMANO_CELDA, y * TAMANO_CELDA))

class Ecosistema:
    def __init__(self):
        self.organismos = []
        self.ambiente = Ambiente()

    def agregar_organismo(self, organismo):
        """Agrega un organismo al ecosistema."""
        self.organismos.append(organismo)

    def ciclo_ecologico(self):
        """Realiza un ciclo completo en el ecosistema."""
        # Actualizar el clima u otros factores abióticos
        self.ambiente.cambiar_clima()

        # Actualizar los organismos en el ecosistema
        for organismo in self.organismos:
            organismo.actuar(self.organismos)

        # Eliminar organismos que han muerto
        self.organismos = [organismo for organismo in self.organismos if organismo.esta_vivo()]

        # Puedes agregar más lógica según sea necesario para mantener el equilibrio ecológico

    def dibujar_ecosistema(self, pantalla):
        """Dibuja el estado actual del ecosistema en la pantalla."""
        pantalla.fill((0, 0, 0))  # Limpia la pantalla antes de dibujar el nuevo frame

        # Dibujar el tablero desde el ambiente
        self.ambiente.dibujar_tablero(pantalla)

        # Dibujar organismos
        for organismo in self.organismos:
            organismo.dibujar(pantalla)

# Iniciar el ecosistema
ecosistema = Ecosistema()

# Variable para controlar el tiempo transcurrido
tiempo_transcurrido = 0
tiempo_cambio_clima = 10000  # 30 segundos en milisegundos

# Bucle principal
corriendo = True
reloj = pygame.time.Clock()

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                # Agrega aquí la lógica que deseas ejecutar cuando se presiona la tecla ESPACIO
                pass

    # Medir el tiempo transcurrido
    tiempo_transcurrido += reloj.tick()

    # Cambiar el clima cada 30 segundos
    if tiempo_transcurrido >= tiempo_cambio_clima:
        ecosistema.ambiente.cambiar_clima()  # Acceder al ambiente a través del ecosistema
        tiempo_transcurrido = 0  # Reiniciar el contador de tiempo

    pantalla.fill((0, 0, 0))  # Limpia la pantalla antes de dibujar el nuevo frame

    # Dibujar el ecosistema
    ecosistema.dibujar_ecosistema(pantalla)

    # Resto del bucle principal (actualización de estado, dibujo, etc.)
    for planta in plantas:
        planta.fotosintesis()  # Actualizar la vida de las plantas
        planta.dibujar_pl(pantalla)
        
    for depredador in [animal for animal in lista_animales if isinstance(animal, Depredador)]:
        depredador.mover(matriz)
        
    for presa in [animal for animal in lista_animales if isinstance(animal, Presa)]:
        print(f"Presa en posición: {presa.posicion}")
        presa.mover(matriz)

    for animal in lista_animales:
        animal.dibujar(pantalla)
    pygame.display.flip()  # Actualiza la pantalla completa

pygame.quit()
sys.exit()