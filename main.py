import pygame
import random 
from random import choice 
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
    1: pygame.image.load('assets/map_images/planta.png'),
    2: pygame.image.load('assets/map_images/arbusto.png'), # Agujero
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

SPRITE_PLANTAS={
    "planta1": pygame.image.load('assets/map_images/planta1.png'),   
    "planta2": pygame.image.load('assets/map_images/planta2.png'),
    "planta3": pygame.image.load("assets/map_images/planta3.png"),
    "planta4": pygame.image.load("assets/map_images/planta4.png"),
    "planta5": pygame.image.load("assets/map_images/planta5.png")     
}

for key, image in SPRITE_PLANTAS.items():
    SPRITE_PLANTAS[key] = pygame.transform.scale(image, (TAMANO_CELDA, TAMANO_CELDA))

# Cargar y escalar imágenes
IMAGENES_NOCHE = {
    0: pygame.image.load('assets/noche/pasto.png'),   # Pasto
    1: pygame.image.load('assets/noche/planta.png'),    # Agujero
    2: pygame.image.load('assets/noche/arbusto.png'),    # Arbusto
    3: pygame.image.load('assets/noche/AguaSupL.png'), 
    4: pygame.image.load('assets/noche/AguaSup.png'), 
    5: pygame.image.load('assets/noche/AguaSupR.png'), 
    6: pygame.image.load('assets/noche/AguaL.png'), 
    7: pygame.image.load('assets/noche/Agua.png'), 
    8: pygame.image.load('assets/noche/AguaR.png'), 
    9: pygame.image.load('assets/noche/AguaAbajoL.png'), 
    10: pygame.image.load('assets/noche/AguaAbajo.png'), 
    11: pygame.image.load('assets/noche/AguaAbajoR.png'), 
    12: pygame.image.load('assets/noche/planta1.png'), 
    
}

for key, image in IMAGENES_NOCHE.items():
    IMAGENES_NOCHE[key] = pygame.transform.scale(image, (TAMANO_CELDA, TAMANO_CELDA))

    
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
    [0,  2,  2,  2, 0, 0, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4], # Fila 2
    [0,  2,  2,  2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #3
    [0,  2,  2,  2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #4
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #5
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#6
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#7
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#8
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#9
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#10
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#11
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0],#12
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0],#13
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#14
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],#15
    [0,  0,  0,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0],#16
    [0,  3,  4,  4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0],#17
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
        self.sprite = SPRITES_ANIMALES.get(especie, None)
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


    def mover(self, matriz):
        # Implementa la lógica de movimiento específica para los depredadores
        # En este ejemplo, el depredador se mueve a una nueva posición cada 1.5 segundos y puede moverse 2 sitios
        tiempo_transcurrido = pygame.time.get_ticks()
        if tiempo_transcurrido - self.ultimo_movimiento >= 1500:  # 1500 milisegundos = 1.5 segundos
            dx, dy = direccion_aleatoria(2)  # Rango de movimiento para el depredador
            nuevo_x = self.posicion[0] + dx
            nuevo_y = self.posicion[1] + dy
            def dibujar(self, pantalla):
                    if self.sprite:
                        pantalla.blit(self.sprite, (self.posicion[0] * TAMANO_CELDA, self.posicion[1] * TAMANO_CELDA))
                    else:
                        pygame.draw.rect(pantalla, (255, 0, 0),
                                        (self.posicion[0] * TAMANO_CELDA, self.posicion[1] * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))
                # Puedes agregar otros métodos específicos de los depredadores si es necesario
            # Verificar si la nueva posición está dentro de los límites de la matriz y si es una celda vacía (valor 0)
            if 0 <= nuevo_x < len(matriz[0]) and 0 <= nuevo_y < len(matriz) and matriz[nuevo_y][nuevo_x] == 0:
                # Actualizar la posición del depredador
                self.posicion = (nuevo_x, nuevo_y)
                self.ultimo_movimiento = tiempo_transcurrido

def posicion_aleatoria_valida(matriz, valores_validos):
    while True:
        x = random.randint(0, len(matriz[0]) - 1)
        y = random.randint(0, len(matriz) - 1)
        if matriz[y][x] in valores_validos:
            return x, y

class Presa(Animal):
    def __init__(self, posicion, vida, energia, velocidad, especie, dieta):
        super().__init__(posicion, vida, energia, velocidad, especie, dieta)

    def dibujar(self, pantalla):
        if self.sprite:
            pantalla.blit(self.sprite, (self.posicion[0] * TAMANO_CELDA, self.posicion[1] * TAMANO_CELDA))
        else:
            pygame.draw.rect(pantalla, (255, 0, 0),
                             (self.posicion[0] * TAMANO_CELDA, self.posicion[1] * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))
            
    # Puedes agregar métodos específicos de las presas si es necesario

    def mover(self, matriz, tiempo_transcurrido):
        self.ultimo_movimiento += tiempo_transcurrido
        if self.ultimo_movimiento >= 2000:
            dx, dy = self.direccion_aleatoria()  # Asumiendo que esta función devuelve un par (dx, dy)
            nuevo_x = self.posicion[0] + dx
            nuevo_y = self.posicion[1] + dy

            # Asegúrate de que la nueva posición esté dentro de los límites y sea una posición válida
            if 0 <= nuevo_x < len(matriz[0]) and 0 <= nuevo_y < len(matriz) and matriz[nuevo_y][nuevo_x] == 0:
                # Actualizar la posición de la presa
                self.posicion = (nuevo_x, nuevo_y)
                # Restablecer el contador de tiempo para el próximo movimiento
                self.ultimo_movimiento = 0

    def huir(self, depredadores, matriz):
        # Comprobar si hay depredadores cerca
        for depredador in depredadores:
            if abs(self.posicion[0] - depredador.posicion[0]) <= 1 and abs(self.posicion[1] - depredador.posicion[1]) <= 1:
                # Moverse en dirección opuesta al depredador
                dx = -(depredador.posicion[0] - self.posicion[0])
                dy = -(depredador.posicion[1] - self.posicion[1])
                self.mover(matriz, dx, dy)

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
    def __init__(self, posicion, vida, energia, tipo, idplanta):
        super().__init__(posicion, vida, energia, velocidad=0)
        self.tipo = tipo
        self.idplanta = idplanta
        self.sprite = SPRITE_PLANTAS.get(f'{tipo}{idplanta}', None)
        self.tiempo_para_reproducirse = 15000  # 15 segundos en milisegundos
        self.tiempo_desde_ultima_reproduccion = 0

    def reproducirse(self, lista_plantas, matriz, valores_cesped_arbustos):
        # Encuentra posiciones adyacentes libres para la nueva planta
        posiciones_adyacentes_libres = [
            (self.posicion[0] + dx, self.posicion[1] + dy)
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            if (dx != 0 or dy != 0)  # Evita la posición actual de la planta
            and 0 <= self.posicion[0] + dx < len(matriz[0])  # Verifica límites horizontales
            and 0 <= self.posicion[1] + dy < len(matriz)     # Verifica límites verticales
            and (self.posicion[0] + dx, self.posicion[1] + dy) not in posiciones_de_plantas  # Verifica que no haya otra planta
            and matriz[self.posicion[1] + dy][self.posicion[0] + dx] in valores_cesped_arbustos
        ]

        # Si hay posiciones libres disponibles
        if posiciones_adyacentes_libres:
            nueva_posicion = random.choice(posiciones_adyacentes_libres)
            # Asumiendo que cada planta tiene un ID único y que idplanta es un entero
            nueva_idplanta = max(planta.idplanta for planta in lista_plantas) + 1
            nueva_planta = Planta(
                nueva_posicion,
                100,  # vida inicial
                50,   # energía inicial
                self.tipo,
                nueva_idplanta
            )
            lista_plantas.append(nueva_planta)
            posiciones_de_plantas.append(nueva_posicion)  # Agregar la nueva posición a la lista de posiciones ocupadas

    def actualizar_tiempo_reproduccion(self, tiempo_transcurrido):
        self.tiempo_desde_ultima_reproduccion += tiempo_transcurrido

posiciones_de_plantas = []
lista_plantas = []

for i in range(5):
    # Añadir depredadores en posiciones aleatorias donde haya pasto o arbustos
    lista_plantas.append(Planta(
        posicion_aleatoria_valida(matriz, valores_cesped_arbustos),
        100,             # vida
        50,              # energía
        "planta",
        str(i+1)    #idplanta
    ))


# Después de cada ciclo en el juego, podrías llamar a la fotosíntesis para cada planta

class Ambiente:
    def __init__(self):
        self.factores = []  # Lista de factores abióticos
        self.es_de_noche = False  # Nuevo atributo para seguir el estado del clima
        self.tiempo_transcurrido = 0  # Nuevo atributo para seguir el tiempo transcurrido
        self.tiempo_cambio_clima = 5000  # Cambiado a 5000 milisegundos para que sea cada 5 segundos

    def cambiar_clima(self):
        self.es_de_noche = not self.es_de_noche  # Cambiar entre True y False
        # Reiniciar el temporizador según el estado del clima
        self.tiempo_transcurrido = 0
    
    def actualizar_tiempo(self, tiempo):
        self.tiempo_transcurrido += tiempo
        # Cambia el clima cada 5 segundos y reinicia el temporizador
        if self.tiempo_transcurrido >= self.tiempo_cambio_clima:
            self.cambiar_clima()
        

    def dibujar_tablero(self, pantalla):
        for y, fila in enumerate(matriz):
            for x, valor in enumerate(fila):
                # Selecciona el diccionario de imágenes según el estado del clima
                imagenes = IMAGENES_NOCHE if self.es_de_noche else IMAGENES
                imagen = imagenes.get(valor)
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
    tiempo_transcurrido = reloj.tick()
    # Cambiar el clima cada 30 segundos
    ecosistema.ambiente.actualizar_tiempo(tiempo_transcurrido)

    # Dibujar el ecosistema
    ecosistema.dibujar_ecosistema(pantalla)

    # Resto del bucle principal (actualización de estado, dibujo, etc.)
        
    for depredador in [animal for animal in lista_animales if isinstance(animal, Depredador)]:
        depredador.mover(matriz)
        
    for presa in [animal for animal in lista_animales if isinstance(animal, Presa)]:
        print(f"Presa en posición: {presa.posicion}")
        presa.mover(matriz, tiempo_transcurrido)  # Pasar tiempo_transcurrido al método mover

    # Aquí es donde manejarás la reproducción de las plantas
    for planta in lista_plantas:
        planta.actualizar_tiempo_reproduccion(tiempo_transcurrido)
        planta.reproducirse(lista_plantas, matriz)
    for animal in lista_animales:
        animal.dibujar(pantalla)
    pygame.display.flip()  # Actualiza la pantalla completa

pygame.quit()
sys.exit()