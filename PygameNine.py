#마우스이동으로 글 혹은 그림 그리기

import sys
import pygame
from pygame.locals import QUIT,MOUSEBUTTONDOWN,MOUSEMOTION,MOUSEBUTTONUP

pygame.init()
SURFACE = pygame.display.set_mode((600,400))
FPSCLOCK = pygame.time.Clock()

def main():
    mousepos= []
    mousedown =False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mousedown = True
            elif event.type ==MOUSEMOTION:
                if mousedown:
                    mousepos.append(event.pos)
            elif event.type == MOUSEBUTTONUP:
                mousedown = False
                mousepos.clear()

        SURFACE.fill((255,255,255))
        if len(mousepos) >1:
            pygame.draw.lines(SURFACE,(255,0,0),False,mousepos)

        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()
