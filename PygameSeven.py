#문자출력하기, 문자크기키우면서 줌인회전시키기

import sys
import pygame
from pygame.locals import QUIT

pygame.init()
SURFACE = pygame.display.set_mode((300,200))
FPSCLOCK = pygame.time.Clock()

def main():
    sysfont = pygame.font.SysFont(None,50)
    message = sysfont.render("Hello worlds!",True, (255,255,255))
    message_rect = message.get_rect()
    theta = 0
    scale = 1

   #message_rect.center =(150,100) 이미지의 중심축 (글자 불러오기시에 필요)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((0,0,0))
        #28 번째 줄부터 33번째 줄까지가 줌인하며 점점크기가 커지며 회전시키는 코드
        theta +=5
        scale = (theta % 360) / 180
        tmp_msg = pygame.transform.rotozoom(message,theta,scale)
        tmp_rect = tmp_msg.get_rect()
        tmp_rect.center=(150,100)
        SURFACE.blit(tmp_msg,tmp_rect)


        pygame.display.update()
        FPSCLOCK.tick(10)

if __name__ == '__main__':
    main()