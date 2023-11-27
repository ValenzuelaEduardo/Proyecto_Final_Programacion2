import pygame

# Inicialización de Pygame
pygame.init()

# Dimensiones de la ventana
ANCHO = 400
ALTO = 400

# Tamaño del cuadrado (celda)
TAMANO_CELDA = 20

# Cargar imágenes
#0 pasto , 1 planta, 2 arbusto , 3 AguaSupL, 4 AguaSup, 5 AguaSupR
#                                 6 AguaL,    7 Agua   , 8 AguaR
#                                 9 AguaAbajoL, 10 AguaAbajo, 11 AguaAbajoR  
# 12 Planta1
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

# Escalar imágenes al tamaño de la celda si es necesario
for key, image in IMAGENES.items():
    IMAGENES[key] = pygame.transform.scale(image, (TAMANO_CELDA, TAMANO_CELDA))

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

# Función para dibujar el tablero
def dibujar_tablero(pantalla):
    for y, fila in enumerate(matriz):
        for x, valor in enumerate(fila):
            imagen = IMAGENES.get(valor)
            if imagen:
                pantalla.blit(imagen, (x * TAMANO_CELDA, y * TAMANO_CELDA))

# Bucle principal del juego
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Dibujar el tablero
    pantalla.fill((0, 0, 0))  # Llenar la pantalla con color negro o cualquier color de fondo
    dibujar_tablero(pantalla)
    pygame.display.flip()  # Actualizar la pantalla completa

# Salir de Pygame y Python
pygame.quit()
