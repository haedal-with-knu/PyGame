
#배경에 원그리기

import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400,250))
FPSCLOCK = pygame.time.Clock()

def main():

    while True:
        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255,255,255))

        #빨간색 : 꽉채워칠한다
        pygame.draw.circle(SURFACE, (255,0,0),(50,50),20)

        #빨간색 : 굵기10
        pygame.draw.circle(SURFACE,(255,0,0,),(150,50),20,10)

        pygame.display.update()
        FPSCLOCK.tick(3)
if __name__ == '__main__':
    main()

#타원그리기
import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400,250))
FPSCLOCK = pygame.time.Clock()

def main():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    SURFACE.fill((255,255,255))#흰색

    #빨간색
    pygame.draw.ellipse(SURFACE,(255,0,0),(50,50,140,60))
    pygame.draw.ellipse(SURFACE, (255,0,0),(250,30,90,90))

    #녹색
    pygame.draw.ellipse(SURFACE, (0, 255, 0),(50,50,140,60), 5)
    pygame.draw.ellipse(SURFACE, (0, 255, 0), ((250, 130), (90, 90)), 20)

    pygame.display.update()
    FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()