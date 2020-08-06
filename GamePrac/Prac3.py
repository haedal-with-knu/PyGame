#네모 박스가 계속 지나가기
import pygame
import sys
from pygame.locals import QUIT,Rect

pygame.init()
WIDTH  = 600
HEIGHT = 600
SURFACE = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Test")
FPSCLOCK = pygame.time.Clock()

def main():
    x_pos = 600
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        x_pos -= 5
        if x_pos < 0:
            x_pos = 600
        SURFACE.fill((0, 0, 0))
        rect = Rect(x_pos, 300, 40, 40)
        pygame.draw.rect(SURFACE, (255, 255, 255),rect)
        pygame.draw.circle(SURFACE,(255,0,0),(x_pos,580),20)
        pygame.display.update()
        FPSCLOCK.tick(60)

if __name__ == "__main__":
    main()