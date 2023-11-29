import pygame
import random

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
    2: pygame.image.load('assets/map_images/arbusto.png'),    # Arbusto
    3: pygame.image.load('assets/map_images/AguaSupL.png'), 
    4: pygame.image.load('assets/map_images/AguaSup.png'), 
    5: pygame.image.load('assets/map_images/AguaSupR.png'), 
    6: pygame.image.load('assets/map_images/AguaL.png'), 
    7: pygame.image.load('assets/map_images/Agua.png'), 
    8: pygame.image.load('assets/map_images/AguaR.png'), 
    9: pygame.image.load('assets/map_images/AguaAbajoL.png'), 
    10: pygame.image.load('assets/map_images/AguaAbajo.png'), 
    11: pygame.image.load('assets/map_images/AguaAbajoR.png'), 
    12: pygame.image.load('assets/map_images/planta1.png'), 
    
}

for key, image in IMAGENES.items():
    IMAGENES[key] = pygame.transform.scale(image, (TAMANO_CELDA, TAMANO_CELDA))
    
SPRITES_ANIMALES = {
    'depredador1': pygame.image.load('assets/depredador/depredador1.png'),
    'depredador2': pygame.image.load('assets/depredador/depredador2.png'),
    'depredador3': pygame.image.load('assets/depredador/depredador3.png'),
    'depredador4': pygame.image.load('assets/depredador/depredador4.png'),
    # ... Añade el resto de los sprites de depredadores
    'normal1': pygame.image.load('assets/presas/normal1.png'),
    'normal2': pygame.image.load('assets/presas/normal2.png'),
    'normal3': pygame.image.load('assets/presas/normal3.png'),
    'normal4': pygame.image.load('assets/presas/normal4.png'),
    'normal5': pygame.image.load('assets/presas/normal5.png'),
    'normal6': pygame.image.load('assets/presas/normal6.png'),
    # ... Añade el resto de los sprites normales
}

for key, image in SPRITES_ANIMALES.items():
    SPRITES_ANIMALES[key] = pygame.transform.scale(image, (TAMANO_CELDA, TAMANO_CELDA))


# Crear la ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
boards = [
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # Fila 1
    [0,  1,  1,  1, 0, 2, 2, 0, 3, 4, 0, 1, 1, 1, 0, 2, 2, 0, 3, 4], # Fila 2
    [0,  0,  0,  0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #3
    [0,  0,  0,  0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #4
    [0,  0,  0,  12, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #5
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#6
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#7
    [0,  0,  0,  0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#8
    [0,  0,  0,  0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#9
    [0,  0,  0,  0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#10
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#11
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#12
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#13
    [0,  0,  0,  12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#14
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#15
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#16
    [0,  3,  4,  4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#17
    [0,  6,  7,  7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#18
    [0,  9,  10, 10, 11, 2, 2, 2, 2, 2, 0, 1, 1, 1, 0, 2, 2, 0, 3, 4], # Fila 19
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Fila 20
]
# Asignamos la matriz a una variable para facilitar su uso
matriz = boards
# Clases del ecosistema

class Organismo:
    def __init__(self, posicion, vida, energia, velocidad):
        self.posicion = posicion  # Posición en el tablero (x, y)
        self.vida = vida          # Vida del organismo
        self.energia = energia    # Energía del organismo
        self.velocidad = velocidad  # Velocidad de movimiento

def direccion_aleatoria(rango_movimiento):
    dx = random.randint(-rango_movimiento, rango_movimiento)
    dy = random.randint(-rango_movimiento, rango_movimiento)
    return dx, dy

class Animal(Organismo):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad)
        self.especie = especie    # Especie del animal
        self.dieta = dieta        # Dieta: Carnívoro, Herbívoro, etc.
        # Aquí elegimos el sprite en función de la especie y la dieta
        self.sprite = SPRITES_ANIMALES.get(f'{especie}{dieta}', None)

    def mover(self, matriz, rango_movimiento):
        dx, dy = direccion_aleatoria(rango_movimiento)
        nueva_x = self.posicion[0] + dx
        nueva_y = self.posicion[1] + dy

        # Verificar si la nueva posición está dentro de los límites del tablero
        if 0 <= nueva_x < len(matriz[0]) and 0 <= nueva_y < len(matriz):
            # Verificar si la celda está libre (es decir, si es pasto o arbusto)
            if matriz[nueva_y][nueva_x] in [0, 2]:
                # Actualizar la posición
                self.posicion = (nueva_x, nueva_y)
                # Aquí podrías decrementar la energía del animal si deseas
                self.energia -= 1
            else:
                # Intentar otra dirección si el lugar está ocupado o no es válido
                self.mover(matriz, rango_movimiento)
        else:
            # Intentar otra dirección si el lugar está fuera de los límites
            self.mover(matriz, rango_movimiento)

    def cazar(self):
        pass
    
    def dibujar(self, pantalla):
        if self.sprite:
            # Dibuja el sprite en la posición correspondiente
            pantalla.blit(self.sprite, (self.posicion[0] * TAMANO_CELDA, self.posicion[1] * TAMANO_CELDA))
        else:
            # Si no hay sprite, podrías dibujar un rectángulo o círculo como placeholder
            pygame.draw.rect(pantalla, (255, 0, 0), (self.posicion[0] * TAMANO_CELDA, self.posicion[1] * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))

class Depredador(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta, presa):
        super().__init__(posicion, vida, energia, velocidad, especie, dieta)
        # Atributo específico para los depredadores
        self.presa = presa  # Especifica la presa que el depredador puede cazar

    def cazar(self):
        # Implementa la lógica de caza aquí
        # Por ejemplo, verifica si hay presas cercanas y realiza alguna acción
        pass

    # Puedes agregar otros métodos específicos de los depredadores si es necesario

def posicion_aleatoria_valida(matriz, valores_validos):
    while True:
        x = random.randint(0, len(matriz[0]) - 1)
        y = random.randint(0, len(matriz) - 1)
        if matriz[y][x] in valores_validos:
            return x, y
        
class Presa(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad, especie, dieta)

    # Puedes agregar métodos específicos de las presas si es necesario

# Ejemplo de uso
# presa1 = Presa((0, 0), 50, 30, 4, "Cebra", "Herbívoro")

        
valores_cesped_arbustos = [0, 2]


lista_animales = []
for i in range(4):
    # Añadir animales en posiciones aleatorias donde haya pasto o arbustos
    lista_animales.append(Animal(
        posicion_aleatoria_valida(matriz, valores_cesped_arbustos),
        100,             # vida
        50,              # energía
        5,               # velocidad
        str(i+1),        # especie
        'DietaEjemplo'   # Proporciona una dieta válida
    ))

for i in range(6):
    # Añadir depredadores en posiciones aleatorias donde haya pasto o arbustos
    lista_animales.append(Depredador(
        posicion_aleatoria_valida(matriz, valores_cesped_arbustos),
        100,             # vida
        50,              # energía
        5,               # velocidad
        'normal',
        'DietaEjemplo',  # Proporciona una dieta válida
        'PresaEjemplo'   # Proporciona una presa válida
    ))


class Planta(Organismo):
    def __init__(self, posicion, vida, energia):
        super().__init__(posicion, vida, energia, velocidad=0)  # Las plantas no se mueven
        self.tipo = 'planta'

    def fotosintesis(self):
        # Asumimos que la fotosíntesis siempre es exitosa por simplicidad
        self.vida += 1  # La planta gana 1 de vida
        self.energia += 1  # También podría ganar energía si así lo deseas

posiciones_de_plantas = []
# Ejemplo de cómo podrías actualizar la vida de las plantas en el juego
# Suponiendo que tienes una lista de todas las plantas en el juego
plantas = [Planta((x, y), vida=5, energia=10) for x, y in posiciones_de_plantas]

# Después de cada ciclo en el juego, podrías llamar a la fotosíntesis para cada planta
for planta in plantas:
    planta.fotosintesis()


    def reproducirse(self):
        # Lógica para la reproducción por semillas
        pass

class Ambiente:
    def __init__(self):
        self.factores = []  # Lista de factores abióticos

    def cambiar_clima(self):
        # Lógica para cambiar el clima
        pass

class Ecosistema:
    def __init__(self):
        self.organismos = []
        self.ambiente = Ambiente()

    def dibujar_tablero(self, pantalla):  # Agrega 'self' y 'pantalla' como argumentos
        for y, fila in enumerate(matriz):
            for x, valor in enumerate(fila):
                imagen = IMAGENES.get(valor)
                if imagen:
                    pantalla.blit(imagen, (x * TAMANO_CELDA, y * TAMANO_CELDA))  # Asegúrate de multiplicar por TAMANO_CELDA

def actualizar_animales(lista_animales, matriz):
    for animal in lista_animales:
        if animal.especie.startswith('depredador'):
            animal.mover(matriz, 3)  # Rango de movimiento para depredadores
        else:
            animal.mover(matriz, 1)  # Rango de movimiento para animales normales

# Iniciar el ecosistema
ecosistema = Ecosistema()

# Bucle principal
# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                # Agrega aquí la lógica que deseas ejecutar cuando se presiona la tecla ESPACIO
                pass

    # Resto del bucle principal (actualización de estado, dibujo, etc.)
    for planta in plantas:
        planta.fotosintesis()  # Actualizar la vida de las plantas

    pantalla.fill((0, 0, 0))  # Limpia la pantalla antes de dibujar el nuevo frame

    # Dibujar el tablero
    ecosistema.dibujar_tablero(pantalla)
    
    # Dibujar animales
    for animal in lista_animales:
        animal.dibujar(pantalla)

    pygame.display.flip()  # Actualiza la pantalla completa

pygame.quit()
