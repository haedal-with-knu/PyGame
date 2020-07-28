import sys
import pygame
import random
import math
from pygame.locals import *

pygame.init()
W = 800
H = 600
SURFACE = pygame.display.set_mode((W,H))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Game : 공피하기')
default_font = pygame.font.Font('NanumGothic.ttf',28)
empty_list =[]


def draw_text(text, font, surface, x, y, main_color):
    text_obj = font.render(text, True,  main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect)
def Ball_Plus:
    #볼이무려 5개! 그러다가 이제얘네가 막 돌거든 그걸 내가 피해 ㅇㅋ? 그리고
    Ball = pygame. display
def ingame():
    global score
    mess_clear = default_font.render("CLEARED!", True, (255,255,0))
    mess_over = default_font.render("GAME OVER!",True, (255,255,0))
    haedal = pygame.image.load('fighter2.png')

def F_Screen():
    start_image = pygame.image.load('haedal.jpg')
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit() #나중에 없앨 코드
            if event.type == KEYDOWN:
                if event.key == pygame.K_q:
                    print('qqq')
                elif event.key == pygame.K_ESCAPE:
                    return 'quit'
        SURFACE.fill((255,255,255))
        SURFACE.blit(start_image, (0, 0))
        draw_text("공 피하기 게임", pygame.font.Font('NanumGothic.ttf',90), SURFACE, W/2, H/3.4, (0,0,0))
        draw_text("시작하시려면 Q를 눌러주세요", default_font, SURFACE, W / 2, H / 2, (0, 0, 0))
        draw_text("종료하시려면 ESC를 눌러주세요", default_font, SURFACE, W / 2, H / 1.3, (0, 0, 0))
        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == "__main__":
    F_Screen()
