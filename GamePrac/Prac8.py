#사방팔방 벽바운드 공

import pygame
import sys
import random
from pygame.locals import QUIT


WIDTH = 600
HEIGHT = 600
pygame.init()
pygame.display.set_caption("Test")
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
FPSCLOCK = pygame.time.Clock()


def main():
    rdx_posx = []
    rdx_posy = []
    rdy_posx = []
    rdy_posy = []
    velocity_y = []
    velocity_x = []
    for i in range(1,15):
        i *= 40
        rdx_posx.append(i)
        rdx_posy.append(0)
        velocity_y.append(random.randint(3, 14))
        rdy_posx.append(0)
        rdy_posy.append(i)
        velocity_x.append(random.randint(3, 14))

    while True:
        SURFACE.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        for i in range(len(rdx_posx)):
            pygame.draw.circle(SURFACE, (255, 255, 0), (rdx_posx[i], rdx_posy[i]), 2)
            pygame.draw.circle(SURFACE, (255, 255, 0), (rdy_posx[i], rdy_posy[i]), 2)
            if rdx_posy[i]<0 or rdx_posy[i] > 600 :
                velocity_y[i] *= -1
            if rdy_posx[i]<0 or rdy_posx[i] > 600 :
                velocity_x[i] *= -1
            rdx_posy[i] += velocity_y[i]
            rdy_posx[i] += velocity_x[i]


        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    main()

