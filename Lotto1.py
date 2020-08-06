'''import random
Lotto = []
for i in range(6):
    b= random.randint(0,9)
    Lotto.append(b)

print(Lotto)'''

import random  # 추가된 모듈
import pygame
import sys
from pygame.locals import KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, QUIT, Rect

pygame.init()
WIDTH  = 600
HEIGHT = 600
pygame.key.set_repeat(15, 15)
SURFACE = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Test")
FPSCLOCK = pygame.time.Clock()

def main():
    pos_x = 30
    pos_y = 570
    x_pos = 600
    y_pos = random.randint(50, 550)
    y1_pos = random.randint(50, 550)
    while True:
        SURFACE.fill((0, 0, 0))
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

            if pos_x < 20:
                pos_x = 20
            elif pos_x > 580:
                pos_x = 580
            if pos_y < 20:
                pos_y = 20
            elif pos_y > 580:
                pos_y = 580
        x_pos -= 5
        if x_pos < 0:
            x_pos = 600
            y_pos = random.randint(50, 550)
            y1_pos = random.randint(50, 550)
        rect = Rect(x_pos, y_pos, 40, 40)
        pygame.draw.rect(SURFACE, (255, 255, 255),rect)
        pygame.draw.circle(SURFACE,(255,0,0),(x_pos,y1_pos),20)
        pygame.draw.circle(SURFACE, (255, 255, 255), (pos_x, pos_y), 20)
        pygame.display.update()
        FPSCLOCK.tick(60)

if __name__ == "__main__":
    main()