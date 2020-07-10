import sys
from math import sin,cos,radians #math 모듈에서 cos,sin,radians를 가져옵니다.
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

        pointlist0 , pointlist1 = [], [] #빈리스트를 생성해줍니다.
        for theta in range(0 , 720, 144): #theta라는 임의의 변수를 0에서부터 144간격으로 720까지 반복합니다.
            rad = radians(theta)
            pointlist0.append((cos(rad)*100 + 100, sin(rad)*100 + 150)) #빈리스트에 값들을 추가해줍니다.
            pointlist1.append((cos(rad)*100 + 300, sin(rad)*100 + 150 ))

        pygame.draw.lines(SURFACE, (0,0,0),True,pointlist0,5) #리스트에 들어가있는 각대로 선을 이어줍니다.
        pygame.draw.aalines(SURFACE, (0,0,0),True,pointlist1,5)

        pygame.display.update()
        FPSCLOCK.tick(20)

if __name__ == '__main__':
    main()