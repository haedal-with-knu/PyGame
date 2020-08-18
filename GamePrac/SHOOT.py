#슈팅 게임

import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_UP,K_DOWN,K_LEFT,K_RIGHT,K_SPACE,K_a,Rect
from time import sleep

pygame.init()
pygame.display.set_caption('SHOOT_GAME')
pygame.key.set_repeat(15,15)
SURFACE = pygame.display.set_mode((1000,600))
FPSCLOCK = pygame.time.Clock()
Big_font = pygame.font.Font('NanumGothic.ttf', 50)
Small_font = pygame.font.Font('NanumGothic.ttf', 20)

class Draw:
    def __init__(self,col,rect,speed = 0):
        self.col = col
        self.rect = rect
        self.speed = speed
    def move(self):
        self.rect.centerx += self.speed
    def draw_E(self):
        pygame.draw.ellipse(SURFACE,self.col,self.rect)
    def draw_R(self):
        pygame.draw.rect(SURFACE,self.col,self.rect)


def Game_Border():
    Start_Point = [(100,150),(100,150),(100,550),(900,150)]
    End_Point = [(100,550),(900,150),(900,550),(900,550)]
    for index in range(len(Start_Point)):
        pygame.draw.line(SURFACE,(255,255,255),Start_Point[index],End_Point[index])

def main():
    game_over = False
    game_start = False
    Score = 0
    Beam_Count = 0
    Cir = Draw((255, 255, 255), Rect(50,300, 30,30))
    Beam = Draw((255, 255, 0), Rect(Cir.rect.centerx, Cir.rect.centery, 5, 5), 10)
    message_Title = Big_font.render("SHOOT_GAME", True, (255, 255, 255))  # 게임제목 적기
    message_Score = Small_font.render("Score: {}".format(Score), True, (255, 255, 255))  # 스코어
    message_game_start = Small_font.render("게임을 시작하시려면 SPACE를 입력하세요", True, (255, 255, 255))  # 게임시작
    message_game_over = Big_font.render("!GAME_OVER!", True, (255, 255, 255))  # 게임오버
    message_caution = Small_font.render("주의 ! 미사일 버튼 : A 미사일은 1개씩 발사됩니다. 2번누를 시 첫 위치부터 발사됨 ",True,(255,255,255))
    while True:
        SURFACE.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    game_start = True
                elif event.key == K_UP:
                    Cir.rect.centery -= 10
                elif event.key == K_DOWN:
                    Cir.rect.centery += 10
                elif event.key == K_a:
                    Beam_Count = 1
                    Beam.rect.center = Cir.rect.center
        if game_start == False:
            SURFACE.blit(message_Title, (350, 200))
            SURFACE.blit(message_game_start, (330, 300))
        else:
            Game_Border()
            Cir.draw_E()
            if Beam_Count == 1:
                Beam.draw_E()
                Beam.move()
                if Beam.rect.centerx >= 900:
                    Beam.rect.center = Cir.rect.center
                    Beam_Count = 0
            if Cir.rect.centery <= 170:
                Cir.rect.centery = 170
            elif Cir.rect.centery >= 530:
                Cir.rect.centery = 530
            SURFACE.blit(message_Title, (350, 20))  # 화면상에 제목 띄우기
            SURFACE.blit(message_Score, (800, 180))  # 화면상에 스코어 띄우기
            SURFACE.blit(message_caution,(170,100))
            if game_over == True:
                SURFACE.blit(message_game_over, (300, 300))
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()