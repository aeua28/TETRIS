import pygame
import sys
import random

# POSICIÓN
class Posicion:
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

# CUADRÍCULA
class Cuadricula:
    def __init__(self):
        self.num_filas = 20
        self.num_columnas = 10
        self.tamaño_celda = 30
        self.cuadricula = [[0 for j in range(self.num_columnas)] for i in range(self.num_filas)]
        self.colores = Colores.get_colores_celdas()

    def print_cuadricula(self):
        for fila in range(self.num_filas):
            for columna in range(self.num_columnas):
                print(self.cuadricula[fila][columna], end="")
            print()

    def draw(self, screen):
        for fila in range(self.num_filas):
            for columna in range(self.num_columnas):
                valor_celda = self.cuadricula[fila][columna]
                rectangulo = pygame.Rect(columna * self.tamaño_celda + 1, fila * self.tamaño_celda + 1, self.tamaño_celda - 1, self.tamaño_celda - 1)
                pygame.draw.rect(screen, self.colores[valor_celda], rectangulo)

# COLORES
class Colores:
    azul = (0, 0, 255) #7
    azul_claro = (0, 255, 255) #1
    naranja = (255, 129, 0) #2
    rojo = (255, 0, 0) #3
    morado = (128, 0, 128) #4
    verde = (0, 255, 0) #5
    amarillo = (255, 255, 0) #6

    @classmethod
    def get_colores_celdas(cls):
        return [cls.azul, cls.azul_claro, cls.naranja, cls.rojo, cls.morado, cls.verde, cls.amarillo]

# BLOQUE
class Bloque:
    def __init__(self, block_id):
        self.id = block_id
        self.celdas = {}  # ES UN DICCIONARIO
        self.tamaño_celda = 30
        self.fila_offset = 0
        self.columna_offset = 0
        self.rotacion = 0
        self.colores = Colores.get_colores_celdas()

    def mover(self, fila, columna):
        self.fila_offset += fila
        self.columna_offset += columna

    def get_posicion_celdas(self):
        tiles = self.celdas[self.rotacion]
        moved_tiles = []
        for posicion in tiles:
            posicion = Posicion(posicion.fila + self.fila_offset, posicion.columna + self.columna_offset)
            moved_tiles.append(posicion)
        return moved_tiles


    def draw(self, screen):
        tiles = self.get_posicion_celdas()
        for tile in tiles:
            tile_rect = pygame.Rect(tile.columna * self.tamaño_celda + 1, tile.fila * self.tamaño_celda + 1, self.tamaño_celda - 1, self.tamaño_celda - 1)
            pygame.draw.rect(screen, self.colores[self.id], tile_rect)

class Juego:
    def __init__(self):
        self.cuadricula=Cuadricula
        self.bloques=[IBloque(),JBloque(),LBloque(),OBloque(),TBloque(),SBloque(),ZBloque()]
        self.bloque_actual=self.get_bloque_random()
        self.siguiente_bloque=self.get_bloque_random()

def get_bloque_random(self):
        if len(self.bloques) == 0:
         self.bloques=[IBloque(),JBloque(),LBloque(),OBloque(),TBloque(),SBloque(),ZBloque()]
        bloque=random.choice(self.bloques)
        self.bloques.remove(bloque)
        return bloque

def draw(self,screen):
    self.cuadricula.draw(screen)
    self.bloque_actual.draw(screen)

# BLOQUE L
class LBloque(Bloque):
    def __init__(self):
        super().__init__(block_id=1)
        self.celdas = {
            0: [Posicion(0, 2), Posicion(1, 0), Posicion(1, 1), Posicion(1, 2)],
            1: [Posicion(0, 0), Posicion(0, 1), Posicion(1, 1), Posicion(2, 1)],
            2: [Posicion(1, 0), Posicion(1, 1), Posicion(1, 2), Posicion(2, 0)],
            3: [Posicion(0, 1), Posicion(1, 2), Posicion(2, 1), Posicion(2, 2)],
        }
        self.mover(0,3)

# BLOQUE T
class TBloque(Bloque):
    def __init__(self):
        super().__init__(block_id=2)
        self.celdas = {
            0: [Posicion(0, 1), Posicion(1, 0), Posicion(1, 1), Posicion(1, 2)],
            1: [Posicion(0, 1), Posicion(1, 1), Posicion(1, 2), Posicion(2, 1)],
            2: [Posicion(1, 0), Posicion(1, 1), Posicion(1, 2), Posicion(2, 1)],
            3: [Posicion(0, 1), Posicion(1, 0), Posicion(1, 1), Posicion(2, 1)],
        }
        self.mover(0,3)

# BLOQUE J
class JBloque(Bloque):
    def __init__(self):
        super().__init__(block_id=3)
        self.celdas = {
            0: [Posicion(0, 0), Posicion(1, 0), Posicion(1, 1), Posicion(1, 2)],
            1: [Posicion(0, 1), Posicion(0, 2), Posicion(1, 1), Posicion(2, 1)],
            2: [Posicion(1, 0), Posicion(1, 1), Posicion(1, 2), Posicion(2, 2)],
            3: [Posicion(0, 1), Posicion(1, 1), Posicion(2, 0), Posicion(2, 1)],
        }
        self.mover(0,3)

# BLOQUE I
class IBloque(Bloque):
    def __init__(self):
        super().__init__(block_id=4)
        self.celdas = {
            0: [Posicion(1, 0), Posicion(1, 1), Posicion(1, 2), Posicion(1, 3)],
            1: [Posicion(0, 2), Posicion(1, 2), Posicion(2, 2), Posicion(3, 2)],
            2: [Posicion(2, 0), Posicion(2, 1), Posicion(2, 2), Posicion(2, 3)],
            3: [Posicion(0, 1), Posicion(1, 1), Posicion(2, 1), Posicion(3, 1)],
        }
        self.mover(-1,3)

# BLOQUE O
class OBloque(Bloque):
    def __init__(self):
        super().__init__(block_id=5)
        self.celdas = {
            0: [Posicion(0, 0), Posicion(0, 1), Posicion(1, 0), Posicion(1, 1)],
            1: [Posicion(0, 0), Posicion(0, 1), Posicion(1, 0), Posicion(1, 1)],
            2: [Posicion(0, 0), Posicion(0, 1), Posicion(1, 0), Posicion(1, 1)],
            3: [Posicion(0, 0), Posicion(0, 1), Posicion(1, 0), Posicion(1, 1)],
        }
        self.mover(0,4)

# BLOQUE S
class SBloque(Bloque):
    def __init__(self):
        super().__init__(block_id=6)
        self.celdas = {
            0: [Posicion(0, 1), Posicion(0, 2), Posicion(1, 0), Posicion(1, 1)],
            1: [Posicion(0, 1), Posicion(1, 1), Posicion(1, 2), Posicion(2, 2)],
            2: [Posicion(1, 1), Posicion(1, 2), Posicion(2, 0), Posicion(2, 1)],
            3: [Posicion(0, 0), Posicion(1, 0), Posicion(1, 1), Posicion(2, 1)],
        }
        self.mover(0,3)

# BLOQUE Z
class ZBloque(Bloque):
    def __init__(self):
        super().__init__(block_id=-1)
        self.celdas = {
            0: [Posicion(0, 0), Posicion(0, 1), Posicion(1, 1), Posicion(1, 2)],
            1: [Posicion(0, 2), Posicion(1, 1), Posicion(1, 2), Posicion(2, 1)],
            2: [Posicion(1, 0), Posicion(1, 1), Posicion(2, 1), Posicion(2, 2)],
            3: [Posicion(0, 1), Posicion(1, 0), Posicion(1, 1), Posicion(2, 0)],
        }
        self.mover(0,3)


# INICIAR
pygame.init()

# VENTANA DEL JUEGO
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("TETRIS")

clock = pygame.time.Clock()

# COLORES DE FICHAS
azul = (0, 0, 255) #7
azul_claro = (0, 255, 255) #1
naranja = (255, 129, 0) #2
rojo = (255, 0, 0) #3
morado = (128, 0, 128) #4
verde = (0, 255, 0) #5
amarillo = (255, 255, 0) #6

# FONDO
azul_oscuro = (0, 47, 167)

# GAME LOOP
cuadricula = Cuadricula()

juego=Juego()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(azul_oscuro)
    juego.draw(screen)

    pygame.display.update()
    clock.tick(70)
