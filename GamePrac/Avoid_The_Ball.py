#떨어지는 공을 피해보기
import pygame
import sys
import random
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN


WIDTH = 600
HEIGHT = 600
pygame.init()
pygame.key.set_repeat(10,10)
pygame.display.set_caption("Test")
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
FPSCLOCK = pygame.time.Clock()


def main():
    Speedx = [1,10,20]
    posx = []
    posy = []
    C_xpos = 300
    C_ypos = 300
    for i in range(1,15):
        i *= 40
        posx.append(i)
    for j in range(1,15):
        j = 600
        posy.append(j)
    while True:
        SURFACE.fill((0, 0, 0))
        pygame.draw.circle(SURFACE, (255,255,255), (C_xpos, C_ypos), 6)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    C_xpos -= 8
                if event.key == K_RIGHT:
                    C_xpos += 8
                if event.key == K_UP:
                    C_ypos -= 8
                if event.key == K_DOWN:
                    C_ypos += 8

        for i in range(len(posx)):
            rd_Speed = random.choice(Speedx)
            posy[i] += rd_Speed
            pygame.draw.circle(SURFACE, (255, 255, 0), (posx[i], posy[i]), 2)
            if posy[i] > 600:
                posy[i] = 0

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    main()