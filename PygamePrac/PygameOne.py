
#배경에 직사각형 그리기
import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()
def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        SURFACE.fill((0,0,0))
        #빨간 직사각형 굵기3
        pygame.draw.rect(SURFACE, (255,0,0), (150,10,100,30),3)
        #초록 직사각형
        pygame.draw.rect(SURFACE, (0,255,0),((100,80),(80,50)))

        rect0= Rect(200,60,140,80)

        pygame.draw.rect(SURFACE,(0,0,255),rect0)

        rect1 = Rect((30,160),(100,50))
        pygame.draw.rect(SURFACE,(255,255,0),rect1)

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__=='__main__':
    main()