import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((800, 800), DOUBLEBUF | OPENGL)
    clock = pygame.time.Clock()
    gluPerspective(45, 1, 0.1, 50)
    glTranslatef(0, 0, -5)
    
    rotate = False
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
        pygame.display.flip()
