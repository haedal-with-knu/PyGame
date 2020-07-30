import sys
import pygame
from pygame.locals import *


k=[]
pygame.init()
SURFACE = pygame.display.set_mode((600,600))
FPSCLOCK = pygame.time.Clock()

def main():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                k.append()

        SURFACE.fill((255,255,255))
        pygame.draw.ellipse(SURFACE,(0,0,0),k)
        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == "__main__":
    main()