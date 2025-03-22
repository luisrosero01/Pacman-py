import pygame
import random
import sys
import tkinter as tk
from tkinter import messagebox

# Inicializar pygame
pygame.init()

# Definir constantes
MAPA_ANCHO = 20
MAPA_ALTO = 9
ANCHO, ALTO = 1200, 800
TAMANO_CELDA = min(ANCHO // MAPA_ANCHO, ALTO // MAPA_ALTO)

pantalla = pygame.display.set_mode((MAPA_ANCHO * TAMANO_CELDA, MAPA_ALTO * TAMANO_CELDA))
pygame.display.set_caption("Pacman")

# Definir colores
NEGRO = (0, 0, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Mapa del juego (0 = vacío, 1 = pared, 2 = punto)
mapa = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]




pac_x, pac_y = 1, 1
fan_x, fan_y = 10, 5
puntos = 0

# Función para reiniciar el juego
def reiniciar_juego():
    global pac_x, pac_y, fan_x, fan_y, puntos, mapa
    pac_x, pac_y = 1, 1
    fan_x, fan_y = 10, 5
    puntos = 0
    mapa = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1],
        [1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 1, 1],
        [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
        [1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 1],
        [1, 2, 2, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

def mover_pacman(dx, dy):
    global pac_x, pac_y, puntos
    nuevo_x, nuevo_y = pac_x + dx, pac_y + dy
    if mapa[nuevo_y][nuevo_x] != 1:  # No atravesar paredes
        pac_x, pac_y = nuevo_x, nuevo_y
        if mapa[pac_y][pac_x] == 2:
            puntos += 1
            mapa[pac_y][pac_x] = 0

def mover_fantasma():
    global fan_x, fan_y
    direcciones = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    random.shuffle(direcciones)
    for dx, dy in direcciones:
        nuevo_x, nuevo_y = fan_x + dx, fan_y + dy
        if mapa[nuevo_y][nuevo_x] != 1:
            fan_x, fan_y = nuevo_x, nuevo_y
            break

def mostrar_game_over():
    root = tk.Tk()
    root.withdraw()
    if messagebox.askyesno("Game Over", "¿Quieres jugar de nuevo?"):
        reiniciar_juego()
    else:
        pygame.quit()
        sys.exit()

def dibujar():
    pantalla.fill(NEGRO)
    for y in range(MAPA_ALTO):
        for x in range(MAPA_ANCHO):
            if mapa[y][x] == 1:
                pygame.draw.rect(pantalla, AZUL, (x * TAMANO_CELDA, y * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))
            elif mapa[y][x] == 2:
                pygame.draw.circle(pantalla, BLANCO, (x * TAMANO_CELDA + TAMANO_CELDA // 2, y * TAMANO_CELDA + TAMANO_CELDA // 2), TAMANO_CELDA // 4)
    pygame.draw.circle(pantalla, AMARILLO, (pac_x * TAMANO_CELDA + TAMANO_CELDA // 2, pac_y * TAMANO_CELDA + TAMANO_CELDA // 2), TAMANO_CELDA // 2)
    pygame.draw.rect(pantalla, ROJO, (fan_x * TAMANO_CELDA, fan_y * TAMANO_CELDA, TAMANO_CELDA, TAMANO_CELDA))

    # Mostrar los puntos
    fuente = pygame.font.Font(None, 36)  # Puedes elegir otra fuente y tamaño
    texto_puntos = fuente.render(f"Puntos: {puntos}", True, BLANCO)
    pantalla.blit(texto_puntos, (10, 10)) #Ajusta la ubicacion

    pygame.display.flip()

# Bucle principal
clock = pygame.time.Clock()
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                mover_pacman(-1, 0)
            elif evento.key == pygame.K_RIGHT:
                mover_pacman(1, 0)
            elif evento.key == pygame.K_UP:
                mover_pacman(0, -1)
            elif evento.key == pygame.K_DOWN:
                mover_pacman(0, 1)
    mover_fantasma()
    if (pac_x, pac_y) == (fan_x, fan_y):
        mostrar_game_over()
    dibujar()
    clock.tick(7)

pygame.quit()
