import pygame
import sys
from pygame.locals import KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN,QUIT

pygame.init()
WIDTH = 600
HEIGHT = 600
pygame.key.set_repeat(15, 15) #키보드키의 연속동작
SURFACE = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Test")
FPSCLOCK = pygame.time.Clock()


def main():
    pos_x = 20
    pos_y = 20
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pos_x -= 10
                if event.key == K_RIGHT:
                    pos_x += 10
                if event.key == K_UP:
                    pos_y -= 10
                if event.key == K_DOWN:
                    pos_y += 10


        SURFACE.fill((0,0,0))
        pygame.draw.circle(SURFACE, (255, 255, 255), (pos_x,pos_y), 20)
        pygame.display.update()
        FPSCLOCK.tick(30)
if __name__ == "__main__":
    main()