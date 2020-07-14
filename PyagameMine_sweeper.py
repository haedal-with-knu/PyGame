import sys
from math import floor
from random import randint
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

WIDTH = 20 #가로방향의 칸수
HEIGHT = 15 #세로방향의 칸수
SIZE =50 #1칸의 가로세로 곱의 크기
NUM_OF_BOMBS = 20 #폭탄수
EMPTY = 0 #맵상의 타일에 아무것도 없는 상태
BOMB = 1 #맵상의 타일에 폭탄이 있는 상태
OPENED =2 # 맵상의 타일이 이미 비어진 상태
OPEN_COUNT = 0 #열린 타일의 수
CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)] #타일의 상태를 이미 확인했는지 기록하는 배열

pygame.init()
SURFACE = pygame.display.set_mode([WIDTH * SIZE, HEIGHT * SIZE])
FPSCLOCK = pygame.time.Clock()

def num_of_bomb(field, x_pos, y_pos):#주위의 폭탄 수를 반환한다.
    #-1 0 1 순으로 좌표를 확인하여 폭탄수를 세어나간다.
    count = 0
    for yoffset in range(-1,2):
        for xoffset in range(-1,2):
            xpos, ypos = (x_pos + xoffset, y_pos+ yoffset)
            if 0 <=xpos <WIDTH and 0<=ypos <HEIGHT and field[ypos][xpos] == BOMB:
                count += 1
    return count

def open_tile(field, x_pos, y_pos):# 타일을 오픈
    global OPEN_COUNT
    if CHECKED[y_pos][x_pos]: #이미 확인된 타일
        return #확인된후 무한반복을 막기위한 return 반환값

    CHECKED[y_pos][x_pos] =True

    for yoffset in range(-1,2):
        for xoffset in range(-1,2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos] == EMPTY:
                field[ypos][xpos] = OPENED
                OPEN_COUNT += 1
                count = num_of_bomb(field,xpos,ypos)
                if count == 0 and not (xpos== x_pos and ypos == y_pos):
                    open_tile(field,xpos,ypos)

def main():
    smallfont = pygame.font.SysFont(None,36)
    largefont = pygame.font.SysFont(None,72)
    message_clear = largefont.render("!!CLEARED", True, (0, 255, 255))
    message_over = largefont.render("!!GAME OVER", True, (0, 255, 255))
    message_rect = message_clear.get_rect()
    message_rect.center = (WIDTH*SIZE/2, HEIGHT*SIZE/2)
    game_over = False

    field = [[EMPTY for xpos in range(WIDTH)] for ypos in range(HEIGHT)]

    #폭탄을 설치, 같은곳에 폭탄을 설치하지않기위한 검사코드
    count = 0
    while count <NUM_OF_BOMBS:
        xpos, ypos = randint(0, WIDTH-1), randint(0, HEIGHT-1)
        if field[ypos][xpos] == EMPTY:
            field[ypos][xpos] = BOMB
            count += 1

    while True:
        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                xpos, ypos = floor(event.pos[0] / SIZE), floor(event.pos[1]/ SIZE)
                if field[ypos][xpos] == BOMB:
                    game_over = True
                else:
                    open_tile(field,xpos,ypos)


        #그리기
        SURFACE.fill((0,0,0))
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                tile = field[ypos][xpos]
                rect = (xpos*SIZE,ypos*SIZE,SIZE,SIZE)

                if tile == EMPTY or tile == BOMB:
                    pygame.draw.rect(SURFACE,(192,192,192),rect)
                    if game_over and tile == BOMB:
                        pygame.draw.ellipse(SURFACE,(225,225,0),rect)
                elif tile == OPENED:
                    count = num_of_bomb(field,xpos,ypos)
                    if count>0:
                        num_image = smallfont.render("{}".format(count),True,(255,255,0))
                        SURFACE.blit(num_image,(xpos*SIZE+10,ypos*SIZE+10))

        # 선 그리기
        for index in range(0,WIDTH*SIZE, SIZE):
            pygame.draw.line(SURFACE, (96,96,96),(index,0),(index,HEIGHT*SIZE))

        for index in range(0, HEIGHT * SIZE, SIZE):
            pygame.draw.line(SURFACE,(96,96,96),(0,index),(WIDTH*SIZE,index))

        #메세지 나타내기
        if OPEN_COUNT == WIDTH *HEIGHT - NUM_OF_BOMBS:
            SURFACE.blit(message_clear,message_rect.topleft)
        elif game_over:
            SURFACE.blit(message_over, message_rect.topleft)

        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == "__main__":
    main()
