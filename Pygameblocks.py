import sys
import math
import random
import pygame
from pygame.locals import *

class Block:
    def __init__(self,col,rect,speed=0): #col:채우는색, rect:그리는 직사각형(위치,크기), speed(이동속도,공만),dir(이동방향, 공만)
        self.col = col
        self.rect = rect
        self.speed = speed
        self.dir = random.randint(-45, 45) +270

    def move(self):#공을 움직인다 , radians를 사용해서 dir을 라디안으로 변환, X축과Y축의 방향성분구분
        self.rect.centerx += math.cos(math.radians(self.dir)) * self.speed
        self.rect.centery -= math.sin(math.radians(self.dir)) * self.speed

    def draw(self):#공, 블럭을 그린다.
        if self.speed == 0:
            pygame.draw.rect(SURFACE, self.col, self.rect)
        else:
            pygame.draw.ellipse(SURFACE, self.col, self.rect)

def tick():#프레임별 처리
    global BLOCKS
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN: #패들 움직이기
            if event.key == K_LEFT:
                PADDLE.rect.centerx -= 10
            elif event.key == K_RIGHT:
                PADDLE.rect.centerx += 10
    if BALL.rect.centery <1000:
        BALL.move()

    #블록과 충돌
    prevlen = len(BLOCKS)
    BLOCKS = [x for x in BLOCKS if not x.rect.colliderect(BALL.rect)]
    if len(BLOCKS) != prevlen:
        BALL.dir *= -1

    #패들과 충돌
    if PADDLE.rect.colliderect(BALL.rect):
        BALL.dir = 90 + (PADDLE.rect.centerx - BALL.rect.centerx) / PADDLE.rect.width * 80

    #벽과 충돌
    if BALL.rect.centerx < 0 or BALL.rect.centerx > 600:
        BALL.dir = 180 - BALL.dir #반사각만큼 방향을 변경시킨다.
    if BALL.rect.centery < 0:
        BALL.dir = -BALL.dir
        BALL.speed = 15

pygame.init()
pygame.key.set_repeat(5, 5)
SURFACE = pygame.display.set_mode((600,800))
FPSCLOCK = pygame.time.Clock()
BLOCKS = []
PADDLE =Block((242,242,0),Rect(300,700,100,30))
BALL = Block((242,242,0), Rect(300,400,20,20),10)

def main():
    myfont = pygame.font.SysFont(None,80)
    mess_clear = myfont.render("CLEARED!", True, (255,255,0))
    mess_over = myfont.render("GAME OVER!",True, (255,255,0))

    fps = 30
    colors = [(255,0,0),(255,165,0),(242,242,0),(0,128,0),(128,0,128),(0,0,250)]
    for ypos,color in enumerate(colors,start =0): #enumerate는 index와 값을 동시에 나열해준다
        for xpos in range(0,5):
            BLOCKS.append(Block(color, Rect(xpos *100 + 60, ypos *50 +40,80,30)))

    while True:
        tick()

        SURFACE.fill((0,0,0))
        BALL.draw()
        PADDLE.draw()
        for block in BLOCKS:
            block.draw()

        if len(BLOCKS) == 0:
            SURFACE.blit(mess_clear,(200,400))
        if BALL.rect.centery > 800 and len(BLOCKS) > 0:
            SURFACE.blit(mess_over, (150,400))

        pygame.display.update()
        FPSCLOCK.tick(fps)

if __name__ == "__main__":
    main()

