#점들을 잇는 선그리기
import random
import sys
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

        SURFACE.fill((0,0,0))

        pointlist= [] #빈리스트를 정해줍니다.
        for _ in range(10):
            xpos = random.randint(0,400) #x와 y값을 임의의 범위에서 정해서 빈리스트에 튜플형식으로 넣어줍니다.
            ypos = random.randint(0,300)
            pointlist.append((xpos,ypos))

        pygame.draw.lines(SURFACE,(255,255,255),True,pointlist, 5)

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()