import random

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from typing import (
    List,
    Tuple
)

def make_shape_info(nbr_shape: int, vertex: Tuple[Tuple[int, int, int]]) -> List[Tuple[Tuple[int, int, int]]]:
    return_value = []
    for shape in range(1, nbr_shape+1):
        current_shape = []
        for vert in vertex:
            current_shape.append(
                tuple(nbr*shape for nbr in vert)
            )

        return_value.append(tuple(current_shape))
    return return_value

def draw_shape(shape_info: Tuple[Tuple[int, int, int]], edge: Tuple[Tuple[int, int, int]]):
    glLineWidth(50)
    glBegin(GL_LINES)
    
    for shape in shape_info:
        for ed in edge:
            for ver in ed:
                glVertex3fv(shape[ver])
    glEnd()


vertex = (
    (-1, -1, -1), # XYZ
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1)
)

edge = (
    (0, 1),
    (0, 3),
    (1, 2),
    (2, 3),

    (4, 5),
    (4, 7),
    (5, 6),
    (6, 7),

    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
)


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((800, 800), DOUBLEBUF | OPENGL)
    clock = pygame.time.Clock()
    gluPerspective(45, 1, 0.1, 50)
    glTranslatef(0, 0, -5)
    
    rotate = False
    shape_info = make_shape_info(5, vertex)

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

            if event.type == KEYDOWN:
                if event.key == K_r:
                    rotate = not rotate

                if event.key == K_z:
                    if rotate:
                        glRotatef(5, 1, 0, 0),
                    else:
                        glTranslatef(0, 0, 1)

                if event.key == K_s:
                    if rotate:
                        glRotatef(5, -1, 0, 0)
                    else:
                        glTranslatef(0, 0, -1)

                if event.key == K_q:
                    if rotate:
                        glRotatef(5, 0, 1, 0)
                    else:
                        glTranslatef(1, 0, 0)

                if event.key == K_d:
                    if rotate:
                        glRotatef(5, 0, -1, 0)
                    else:
                        glTranslatef(-1, 0, 0)
                        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_shape(shape_info, edge)
        pygame.display.flip()
