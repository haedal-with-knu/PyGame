# 주요코드 설명하기
import sys #sys모듈을 가져옵니다.
import pygame #pygame을 만들기 위한 모듈을 가져옵니다.
from pygame.locals import QUIT #pygame.locals 중에서 게임을 종료하기위한 QUIT 모듈을 끌어옵니다

pygame.init() #pygame의 초깃값을 설정해줍니다.
SURFACE = pygame.display.set_mode((400,300)) #pygame의 화면을 띄운다
FPSCLOCK = pygame.time.Clock() #pygame의 시간을 설정한다.

def main():
    while True:
        for event in pygame.event.get(): #event타입을 불러온다
            if event.type == QUIT: #만일 event타입키가 QUIT이라면 게임과 화면을 종료한다.
                pygame.quit()
                sys.exit()

        SURFACE.fill((255,255,255)) #화면을 블랙으로 채운다. 단, 색은 지정값에따라 바뀔수있음.

        pygame.display.update()  #게임을 실행해줍니다.
        FPSCLOCK.tick(20) #게임의 프레임을 정해줍니다.

if __name__ == "__main__": #__name__ == "__main__"은 인터프리터에서 직접 실행했을 경우에만 if문 내의 코드르 실행하라
    main()