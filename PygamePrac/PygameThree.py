#선그리기

import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,220))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255,255,255))

        #빨간색 가로줄
        pygame.draw.line(SURFACE,(255,0,0),(10,80),(200,80),20)#(색,시작점<-((x,y)표시),끝점<-((x,y)표시)),굵기

        #파란색 빗금
        start_pos = (300,30)
        end_pos = (380,200)
        pygame.draw.line(SURFACE,(0,0,255),start_pos,end_pos,10)

        pygame.display.update()
        FPSCLOCK.tick(3)
if __name__ == '__main__':
    main()

# 격자모양만들기

import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255,255,255))
        #범위에 맞게 선을 그어줍니다.
        for xpos in range(0,400,25):
            pygame.draw.line(SURFACE,(255,0,0),(xpos,0),(xpos,300))

        for ypos in range(0,300,25):
            pygame.draw.line(SURFACE,(255,0,0),(0,ypos),(400,ypos))

        pygame.display.update()
        FPSCLOCK.tick(3)
if __name__ == '__main__':
    main()