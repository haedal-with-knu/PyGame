import pygame
import sys
import math
import random
from pygame.locals import QUIT, Rect

pos_x = []
pos_y = []
x_pos = random.randint(20, 580)
y1_pos = random.randint(20, 580)
y_pos = 600
x1_pos = 600
BALL_x = []
BALL_y = []
WIDTH = 600
HEIGHT = 600
pygame.init()
pygame.display.set_caption("Test")
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
FPSCLOCK = pygame.time.Clock()

def draw():
    global x_pos
    global y1_pos
    for j in range(4):
        for i in range(4):
            pos_x.append((x_pos, y_pos))
            pos_y.append((x1_pos, y1_pos))
            if pos_x[i] not in pos_x:
                pos_x.append((x_pos, y_pos))
            if pos_y[i] not in pos_y:
                pos_y.append((x1_pos, y1_pos))
            BALL_x.append(pygame.draw.circle(SURFACE,(255,255,0),(pos_x[i]),3))
            BALL_y.append(pygame.draw.circle(SURFACE,(255,255,0),(pos_y[i]),3))

def main():
    global y_pos
    global x1_pos
    while True:
        SURFACE.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        y_pos -= 5
        x1_pos -= 5
        if y_pos <0 :
            y_pos =600
        if x1_pos <0:
            x1_pos =600
        for i in range(4):
            draw()
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    main()
