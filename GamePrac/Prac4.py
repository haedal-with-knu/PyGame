#네모 박스가 계속 지나가기
import random  # 추가된 모듈
import pygame
import sys
from pygame.locals import QUIT,Rect

pygame.init()
WIDTH  = 600
HEIGHT = 600
SURFACE = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Test")
FPSCLOCK = pygame.time.Clock()

def main():
    x_pos = 600
    y_pos = random.randint(40, 560)
    y1_pos = random.randint(40, 560)
    while True:
        SURFACE.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        x_pos -= 5
        if x_pos < 0:
            x_pos = 600
            y_pos = random.randint(40, 560)
            y1_pos = random.randint(40, 560)
            if abs(y_pos-y1_pos)<= 50: #절대값을 주어 둘의 뺄셈값이 50이하라면 다시 y좌표를 설정합니다.
                y_pos = random.randint(40, 560)
                y1_pos = random.randint(40, 560)
        rect = Rect(x_pos, y_pos, 40, 40)
        pygame.draw.rect(SURFACE, (255, 255, 255),rect)
        pygame.draw.circle(SURFACE,(255,0,0),(x_pos,y1_pos),20)
        pygame.display.update()
        FPSCLOCK.tick(60)

if __name__ == "__main__":
    main()