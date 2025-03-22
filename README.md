# Pacman-py

Se ha usado *Python* para hacer una replica similar a Pacman, juego de los 80 creado originalmente por *Namco*

## Explicación del código

# Librerías:

Usamos `import` para importar las siguentes librerías:

- Pygame (Se usa para desarrollar juegos en Python. Se encarga de la gestión de gráficos, sonido, eventos de teclado/ratón, etc.)
- Random (Sirve para generar aleatoriedad con números. Esto más adelante se usa para generar los movimientos del fantasma)
- Sys (Es un módulo preinstalado con Python. Da acceso a variables y funciones del sistema. Sin esto, no se podrá cerrar el juego)
- Tkinter (Para crear una ventana de diálogo que pregunta al usuario si quiere jugar de nuevo, una vez que el Pacman (El circulo amarillo/jugador) colisiona con el fantasma rojo)

# Constantes y módulos fundamentales:

- `pygame.init()`: Inicia todos los módulos de Pygame. La consola de Python dará error si se usa cualquier módulo de Pygame antes de `pygame.init()`
- `MAPA_ANCHO`, `MAPA_ALTO`: Definen las dimensiones del mapa del juego
- `ANCHO`, `ALTO`: Definen la resolución de la ventana del juego (1200x800).
- `TAMANO_CELDA`: Calcula el tamaño de cada celda del mapa, dividiendo las dimensiones de la ventana entre las dimensiones del mapa.  Se usa `min()` para que las celdas quepan tanto en el ancho como en el alto de la ventana.
- `pantalla = pygame.display.set_mode((MAPA_ANCHO * TAMANO_CELDA, MAPA_ALTO * TAMANO_CELDA))`: Crea la ventana del juego con las dimensiones calculadas. Se crea una "pantalla" donde se va a dibujar los objetos geométricos del Pacman y del fantasma.
- `pygame.display.set_caption("Pacman")`: Aparece un nombre en la ventana del juego en ejecución
- `NEGRO`, `AZUL`, `AMARILLO`, `BLANCO`, `ROJO`: Definen los colores en formato RGB, el valor tiene que ser un número natural que no sea menor que 0 y mayor que 255

# `mapa`: 
Es una lista de listas que es prácticamente el laberinto/nivel del juego.

```python
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
```
`0`: Celda vacía donde el Pacman y el fantasma se pueden mover.
`1`: Representa la pared del juego, el jugador, ni el fantasma no podrán atraversarlos.
`2`: Es el punto que el jugador puede recolectar. Al hacerlo, se le suma +1 punto.
`pac_x`, `pac_y`: Coordenadas iniciales de Pacman (fila 1, columna 1).
`fan_x`, `fan_y`: Coordenadas iniciales del fantasma (fila 5, columna 10).
`puntos`: Puntuación inicial del jugador (0).

## Funciones:

# def `reiniciar_juego()`:
Reinicia todo el juego de forma automática, esto quiere decir que los puntos recogidos se convierten en cero, las posiciones del fantasma y del Pacman (El jugador) se reestablecen, y los puntos que se recogieron en la anterior partida, vuelven a aparecer. Muy importante para poder volver a jugar sin tener que cerrar y abrir el juego de nuevo.


# def `mover_pacman(dx, dy)`:

`global pac_x, pac_y, puntos`: Índica que se modificarán las variables globales.

`dx`, `dy`: Representan el cambio de posición en x, y. Por ejemplo, `dx = 1` equivale a moverse una celda a la derecha, `dy = -1` dará cómo resultado que el Pacman se mueva una celda hacia arriba.

`nuevo_x, nuevo_y`: Calcula las nuevas coordenadas potenciales de Pacman.

`if mapa[nuevo_y][nuevo_x] != 1:`: Verifica si la nueva posición es válida (no es una pared).

`pac_x, pac_y = nuevo_x, nuevo_y`: Si la nueva posición es válida, entonces se actualizará las coordenadas del Pacman.

`if mapa[pac_y][pac_x] == 2:`:  Verifica si Pacman se ha movido a una celda que contiene un punto.

`puntos += 1`: Si se cumple la condición de los puntos, se incrementa la puntuación.

`mapa[pac_y][pac_x] = 0`:  Visualmente se "elimina" el punto del mapa, pero lo que en realidad hace es reemplazarlo por un espacio vacío.


# def `mover_fantasma()`:

`global fan_x, fan_y`:  Indica que se modificarán las variables globales.

`direcciones`:  Una lista de tuplas que representan los cuatro posibles movimientos: arriba, abajo, izquierda, derecha.

`random.shuffle(direcciones)`:  Mezcla aleatoriamente el orden de las direcciones del fantasma.

`for dx, dy in direcciones:`: Itera a través de las direcciones (arriba, abajo, izquierda, derecha) mezcladas.

`nuevo_x, nuevo_y`: Calcula las nuevas coordenadas potenciales del fantasma.

`if mapa[nuevo_y][nuevo_x] != 1:`: Verifica si la nueva posición es válida.

`fan_x, fan_y = nuevo_x, nuevo_y`: Si se cumple, actualiza las coordenadas del fantasma.

`break`:  Sale del bucle `for` después de que el fantasma se haya movido.


# def`mostrar_game_over()`:

`root = tk.Tk()`:Crea una ventana raíz de Tkinter .
`root.withdraw()`: Oculta la ventana raíz
`messagebox.askyesno("Game Over", "¿Quieres jugar de nuevo?")`: Muestra un cuadro de diálogo. Internamente, dará `True` si se hace clic en "Sí" y llamara la función de `reiniciar_juego()`. De lo contrario, si el usuario "No" desea jugar de nuevo el juego, se marcará como `False` y se cerrará el programa y el Pygame

# def `dibujar()`:

`pantalla.fill(NEGRO)`: Rellena toda la pantalla de negro.

 Doble bucle `for`: Itera sobre cada celda del mapa (`y` para las filas, `x` en las columnas). Si la celda es una pared (`mapa[y][x] == 1`), dibuja un rectángulo azul. En cambio si la celda es un punto (`mapa[y][x] == 2`), dibuja un círculo blanco. 
 
``pygame.draw.circle` Dibuja un circulo amarillo para representar al Pacman.
``pygame.draw.rect()` Dibuja un rectángulo rojo, en la posición del fantasma.
 
 Dibuja los puntos en la esquina superior con:
`fuente = pygame.font.Font(None, 36)`: Elige la fuente. `None` significa predeterminado y `36` el tamaño.
`texto_puntos = fuente.render(f"Puntos: {puntos}", True, BLANCO)`: Crea una superficie de texto con el resultado de los puntos. `True` es antialising, y `BLANCO` es el color.
`pantalla.blit(texto_puntos, (10, 10))`: Dibuja el texto en la pantalla, en las coordenadas X, Y (10, 10).
`pygame.display.flip()`: Actualiza completamente la pantalla.


## Bucle Principal del Juego:

`clock = pygame.time.Clock()`: Crea un objeto `Clock` que se utiliza para controlar la velocidad del juego (fotogramas por segundo).

`corriendo = True`: Variable booleana que controla si el juego se está ejecutando.

`while corriendo:`: Bucle principal del juego. Se ejecuta continuamente hasta que `corriendo` sea lo contrario, o sea, cuando el valor pase a `False`.

`for evento in pygame.event.get()`: Obtiene todos los eventos ocurridos desde la última vez que se llamó a `pygame.event.get()`. Ya sean pulsaciones de teclas, movimientos del ratón, clics, etc.

`if evento.type == pygame.QUIT:`: Si el evento es de tipo `QUIT` (Por ejemplo si pulsa ALT + F4 o cierra la ventana del juego), entonces la variable booleana de `corriendo` pasa a convertirse a `False` para salir del bucle principal.

`elif evento.type == pygame.KEYDOWN:`: Si el evento es una tecla presionada, comprueba qué tecla se ha presionado (`evento.key`). Si es una flecha (izquierda, derecha, arriba, abajo), llamará a `mover_pacman()` con el desplazamiento apropiado.

`mover_fantasma()`: Llama a la función para mover el fantasma rojo.

`if (pac_x, pac_y) == (fan_x, fan_y):`: Comprueba si el Pacman colisiona con el fantasma rojo. Si se cumple esa condición, llama a `mostrar_game_over()`.

`dibujar()`: Llama a la función para dibujar todo en la pantalla.

`clock.tick(7)`: Es la que limita la velocidad del juego, en este caso está a 7 fotogramas por segundo.

`pygame.quit()`: Se cierra Pygame, después de salir del bucle principal
