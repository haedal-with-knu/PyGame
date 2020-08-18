#게임 화면 만들기
import pygame
import sys
from pygame.locals import QUIT

pygame.init()
pygame.display.set_caption('Pygame')
SURFACE = pygame.display.set_mode((1000,600))
FPSCLOCK = pygame.time.Clock()

def Game_Border():
    Start_Point = [(100,100),(100,100),(100,500),(900,100)]
    End_Point = [(100,500),(900,100),(900,500),(900,500)]
    for index in range(len(Start_Point)):
        pygame.draw.line(SURFACE,(255,255,255),Start_Point[index],End_Point[index])
def main():
    Score = 0
    Big_font = pygame.font.SysFont('None',50)
    Small_font = pygame.font.SysFont('None',30)
    message_Title = Big_font.render("Game_Title",True,(255,255,255)) # 게임제목 적기
    message_Score = Small_font.render("Score: {}".format(Score),True,(255,255,255))#스코어
    while True:
        SURFACE.fill((0,0,0))
        SURFACE.blit(message_Title,(400,20))#화면상에 제목 띄우기
        SURFACE.blit(message_Score,(800,60))#화면상에 스코어 띄우기
        Game_Border()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()