import sys
import pygame
import random
import math
from pygame.locals import QUIT, KEYDOWN, K_LEFT,K_RIGHT,K_UP,K_DOWN, K_SPACE,Rect


class Block:
    def __init__(self,col,rect,speed = 0): #col:채우는색, rect:그리는 직사각형(위치,크기), speed(이동속도,공만),dir(이동방향, 공만)
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-90, 90) +215

    def move(self):#공을 움직인다 , radians를 사용해서 dir을 라디안으로 변환, X축과Y축의 방향성분구분
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed
    def draw(self):
        pygame.draw.ellipse(SURFACE, self.col, self.rect)

WIDTH = 600
HEIGHT = 600
pygame.init()
pygame.key.set_repeat(10,10)
SURFACE = pygame.display.set_mode((WIDTH,HEIGHT))
FPSCLOCK = pygame.time.Clock()



def main():
    game_start = False
    game_over = False
    velocity = []
    rd_pos = []
    zero_pos = []
    Ball_x = []
    Ball_y = []
    for i in range(1, 30):
        i *= 20
        rd_pos.append(i)
        zero_pos.append(0)
        velocity.append(random.randint(3,8))
    posx = 300
    posy = 300
    Cir = Block((255,255,255), Rect(posx, posy, 8, 8))
    Small_font = pygame.font.Font('NanumGothic.ttf',20)
    Big_font = pygame.font.Font('NanumGothic.ttf', 40)
    message_start = Small_font.render("Game을 시작하시려면 SPACE_BAR를 누르세요",True,(255,255,255))
    message_over = Big_font.render("Game Over", True, (255, 255, 255))


    while True:
        SURFACE.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    Cir.rect.centerx -= 10
                if event.key == K_RIGHT:
                    Cir.rect.centerx += 10
                if event.key == K_UP:
                    Cir.rect.centery -= 10
                if event.key == K_DOWN:
                    Cir.rect.centery += 10
                if event.key == K_SPACE:
                    game_start = True
        if game_start == False:
            SURFACE.blit(message_start, (100, 300))
        else:
            Cir.draw()
            if game_over == True:
                SURFACE.blit(message_over,(200,300))
            if Cir.rect.centerx > 590:
                Cir.rect.centerx = 590
            elif Cir.rect.centerx <10:
                Cir.rect.centerx =10
            if Cir.rect.centery > 590:
                Cir.rect.centery= 590
            elif Cir.rect.centery <10:
                Cir.rect.centery =10

            for i in range(len(rd_pos)):
                Ball_x.append(Block((255, 255, 0), Rect(rd_pos[i], zero_pos[i], 2, 2),velocity[i]))
                Ball_y.append(Block((255, 255, 0), Rect(zero_pos[i], rd_pos[i], 2, 2),velocity[i]))
                Ball_x[i].draw()
                Ball_y[i].draw()
                if Ball_x[i].rect.centery < 1000:
                    Ball_x[i].move()
                if Ball_y[i].rect.centery < 1000:
                    Ball_y[i].move()

                if Ball_x[i].rect.centery < 0 or Ball_x[i].rect.centery >600:
                    Ball_x[i].dir = - Ball_x[i].dir
                if Ball_y[i].rect.centery < 0 or Ball_y[i].rect.centery > 600:
                    Ball_y[i].dir = - Ball_y[i].dir
                if Ball_x[i].rect.centerx < 0 or Ball_x[i].rect.centerx >600:
                    Ball_x[i].dir = 180 - Ball_x[i].dir
                if Ball_y[i].rect.centerx < 0 or Ball_y[i].rect.centerx > 600:
                    Ball_y[i].dir = 180 - Ball_y[i].dir

                if Cir.rect.colliderect(Ball_x[i].rect) or Cir.rect.colliderect(Ball_y[i].rect):
                    game_over = True
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    main()
