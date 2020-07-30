import sys
import pygame
from math import floor
from pygame.locals import *

xpos =0
ypos =0
x_pos =0
y_pos =0
BLACK = []
WHITE = []
WIDTH = 30
HEIGHT = 30
SIZE = 30
OPENED =2
OPEN_COUNT = 0
CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

pygame.init()
SURFACE = pygame.display.set_mode((600,600))
FPSCLOCK = pygame.time.Clock()

def main():
    Myfont = pygame.font.Font("NanumGothic.ttf",40)
    Black_win = Myfont.render("흑의 승리!!",True,(0,255,255))
    White_win = Myfont.render("백의 승리!!",True,(0,255,255))
    WIN_rect = Black_win.get_rect()
    WIN_rect.center = (WIDTH * SIZE /2, HEIGHT * SIZE/2)
    Game_End = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                xpos, ypos = floor(event.pos[0] / SIZE), floor(event.pos[1] / SIZE)
                BLACK.append(xpos,ypos)
            elif event.type == MOUSEBUTTONDOWN and event.button == 3:
                x_pos, y_pos = floor(event.pos[0] / SIZE), floor(event.pos[1] / SIZE)
                WHITE.append(x_pos,y_pos)
        SURFACE.fill((170,90,48))
        pygame.draw.ellipse(SURFACE,(0,0,0),(xpos,ypos))
        pygame.draw.ellipse(SURFACE,(255,255,255),(x_pos,y_pos))
        for index in range(0,WIDTH*SIZE,SIZE):
            pygame.draw.line(SURFACE,(0,0,0),(index, 0),(index, HEIGHT*SIZE))
        for index in range(0, HEIGHT * SIZE, SIZE):
            pygame.draw.line(SURFACE, (0,0,0), ( 0, index), (WIDTH * SIZE, index))

        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == '__main__':
    main()