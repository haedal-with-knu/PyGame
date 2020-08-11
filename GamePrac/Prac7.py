# 속도가 다른 공 10개 생성하여 속도가 다르게 지나가기

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
    Speedy = [1,10,20]
    posx = []
    posy = []
    for i in range(1,15):
        i *= 40
        posy.append(i)
    for j in range(1,15):
        j = 600
        posx.append(j)
    while True:
        SURFACE.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        for i in range(len(posx)):
            rd_Speed = random.choice(Speedy)
            posx[i] += rd_Speed
            pygame.draw.circle(SURFACE, (255, 255, 0), (posx[i], posy[i]), 2)
            if posx[i] > 600:
                posx[i] = 0

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    main()

