import sys
from random import *
import pygame
from pygame.locals import *

pygame.init()
pygame.key.set_repeat(5,5)
SURFACE = pygame.display.set_mode((600,600))
FPSCLOCK = pygame.time.Clock()

def main():
    charicter_image = pygame.image.load("./PySpaceship/spaceship.png")
    obstacle_image = pygame.image.load("./img/start.png")
    sysfont = pygame.font.SysFont(None,36)
    score = 0
    velocity = 0
    hole = []
    game_over = False
    while True:
        is_space_down = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    is_space_down = True

        #캐릭이동
        if not game_over:
            if #캐릭이 장애물을 뛰어넘엇을때
                score += 10


            #동굴스크롤
            edge = holes[-1].copy()
            test = edge.move
