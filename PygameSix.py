#이미지 붙여넣고 회전시키기

import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400,300))
FPSCLOCk = pygame.time.Clock()

def main():
    logo = pygame.image.load("./img/pythonlogo.jpg")
    theta = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        theta +=1
        SURFACE.fill((225,225,225))
        
        #SURFACE.blit(logo,(x,y)) 만 존재할시 회전없이 사진만 불러오기 가능

        new_logo = pygame.transform.rotate(logo,theta) #로고를 커지는 theta만큼 회전시킨다
        rect = new_logo.get_rect()
        rect.center=(200,150) #중심축을 정하는 코드
        SURFACE.blit(new_logo,rect)

        pygame.display.update()
        FPSCLOCk.tick(30)

if __name__ == '__main__':
    main()