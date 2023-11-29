# Proyecto_Final_Programacion2

guia de instalacion

1. Instalar Python:

Si aún no tienes Python instalado, puedes descargarlo desde el sitio web oficial: https://www.python.org/downloads/release/python-3120/.

(el link usa la ultima version de python lanzada hasta la fecha de hoy 29 de noviembre del año 2023)

Durante la instalación, asegúrate de marcar la opción que dice "Add Python to PATH" (Agregar Python al PATH) para facilitar el uso de Python desde la línea de comandos.

2. Instalar pygame:
Abre una terminal o símbolo del sistema y ejecuta el siguiente comando para instalar pygame usando pip (el gestor de paquetes de Python):

pip install pygame o pip3 install pygame

Este comando descargará e instalará la biblioteca pygame y todas las dependencias necesarias.

3. Verificar la instalación de pygame:
Puedes verificar que pygame se ha instalado correctamente ejecutando un pequeño script de prueba. Crea un archivo llamado test_pygame.py y agrega el siguiente código:

import pygame

pygame.init()

# Crear una ventana
pantalla = pygame.display.set_mode((400, 300))

# Mantener la ventana abierta
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pygame.display.flip()

pygame.quit()
Guarda el archivo y ejecútalo desde la terminal de vscode o de tu editor de texto o en su defecto desde el símbolo del sistema:

python test_pygame.py

Deberías ver una ventana simple que se abre y se cierra al hacer clic en el botón de cerrar.

4. Instalar random y sys (si es necesario):
random y sys son módulos estándar de Python, por lo que generalmente no necesitas instalarlos por separado. Puedes importarlos directamente en tu código sin realizar ninguna instalación adicional:

import random
import sys

o si lo pide pip3 install sys y pip3 install random