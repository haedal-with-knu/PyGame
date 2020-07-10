#폴라곤 그리기

import sys
from math import sin, cos, radians
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255,255,255))

        pointlist0, pointlist1 = [],[]

        for theta in range(0,360,72): #오각형을 그리기위한 각도를 지정해줍니다.
            rad = radians(theta)
            pointlist0.append((cos(rad)*100 + 100, sin(rad)*100 + 150)) #빈리스트에 정해진 각도들을 넣어줍니다.
            pointlist1.append((cos(rad)*100 + 300, sin(rad)*100 + 150))

        pygame.draw.lines(SURFACE, (0,0,0),True, pointlist0)
        pygame.draw.polygon(SURFACE,(0,0,0), pointlist1)

        pygame.display.update()
        FPSCLOCK.tick(5)

if __name__ == "__main__":
    main()