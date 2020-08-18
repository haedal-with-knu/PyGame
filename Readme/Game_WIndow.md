## 게임화면틀을 이쁘게 만들어 보자!

<br>

![게임 화면 만들기](../img/게임화면.PNG)

<br>

###코드설명

 + ### [게임화면 코드](../GamePrac/Game_Windows.py)
 
```buildoutcfg
#게임 화면 만들기
import pygame
import sys
from pygame.locals import QUIT

pygame.init()
pygame.display.set_caption('Pygame') # 화면맨위 바에 뜨는 이름
SURFACE = pygame.display.set_mode((1000,600)) 가로 1000px 세로 600px
FPSCLOCK = pygame.time.Clock()
```

<br>

 + 화면 구성을 위한 모듈과 화면을 생성하고 프레임을 받을 변수를 만들어 줍니다.
 
 <br>
 
 ```buildoutcfg
# 게임화면을 구분하기 위한 테두리 생성
def Game_Border():
    Start_Point = [(100,100),(100,100),(100,500),(900,100)]
    End_Point = [(100,500),(900,100),(900,500),(900,500)]
    for index in range(len(Start_Point)):
        pygame.draw.line(SURFACE,(255,255,255),Start_Point[index],End_Point[index])
```

<br>

 + 시작지점과 끝지점을 생성하여 선을 이어줍니다.
 
 <br>
 
 ```buildoutcfg
def main():
    Score = 0
    Big_font = pygame.font.SysFont('None',50)
    Small_font = pygame.font.SysFont('None',30)
    message_Title = Big_font.render("Game_Title",True,(255,255,255)) # 게임제목 적기
    message_Score = Small_font.render("Score: {}".format(Score),True,(255,255,255))#스코어
```

<br>

 + 스코어를 기록할 변수와 제목을 적을 폰트의 종류 스코어를 표시할 폰트의 종류와 크기를 정해줍니다.
그리고 화면에 띄울 메세지를 저장합니다.

<br>

```buildoutcfg
    #화면그리기
    while True:
        SURFACE.fill((0,0,0))
        SURFACE.blit(message_Title,(400,20))#좌표를 통해 화면상에 제목 띄우기
        SURFACE.blit(message_Score,(800,60))#좌표를 통해 화면상에 스코어 띄우기
        Game_Border()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()
```

<br>

 + 이러면 게임화면을 완성 하실 수 있습니다.