# 화면상의 도형움직이기

 + [도형움직이기](../GamePrac/Prac1.py) 

 + 간단하게 화면상의 원을 방향키를 사용하여 움직입니다.
 
```buildoutcfg
import pygame
import sys
from pygame.locals import KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN,QUIT
```

<br>

 + 파이게임, 시스템 모듈을 가져옵니다. 그리고 방향키를 눌렀을 때 방향키를 사용하고 창을 닫으면 게임이 종료되는 기능을 가져옵니다.
 
 <br>
 
 ```buildoutcfg
pygame.init()
WIDTH = 600
HEIGHT = 600
pygame.key.set_repeat(15, 15) #키보드키의 연속동작
SURFACE = pygame.display.set_mode((WIDTH,HEIGHT)) #화면의 크기
pygame.display.set_caption("Test") #게임의 이름정하기
FPSCLOCK = pygame.time.Clock() ##pygame의 프레임을 설정한다
```

<br>

 + pygame.init()는 파이게임의 초기화를 설정해줍니다. 반드시 필요한 코드입니다.
 그리고 WIDTH와 HEIGHT는 화면의 크기를 정해줍니다. 여기서
 'pygame.key.set_repeat'이 있는 데 이것은 키보드키를 꾹눌렀을때 계속 작동하게 해주는 코드입니다.
 
 <br>
 
 + 다음은 main함수에 대해서 알아봅시다.
 
 ```buildoutcfg
def main():
    pos_x = 20
    pos_y = 20
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
```

<br>
 
+ 변수로써 pos_x,pos_y의 기본값을 설정해줍니다. 그리고 파이게임의 이벤트속성을 가지고와서
QUIT를 지정해줍니다. 파이게임창을 닫을 시에 파이게임시스템이 종료됩니다.

<br>

```buildoutcfg
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pos_x -= 10
                if event.key == K_RIGHT:
                    pos_x += 10
                if event.key == K_UP:
                    pos_y -= 10
                if event.key == K_DOWN:
                    pos_y += 10
```

<br>

 + 이벤트 타입이 키를 누르는 것일때, 방향키 이용하여 상하좌우 움직이게하고 그만큼의 좌표를 바꾸어줍니다.
 
<br>

```buildoutcfg
        SURFACE.fill((0,0,0))
        pygame.draw.circle(SURFACE, (255, 255, 255), (pos_x,pos_y), 20)
        pygame.display.update()
        FPSCLOCK.tick(30)
```

<br>

 + 화면을 검은색으로 가득채우고 draw기능을 활용하여 화면에 원을 그립니다.
 pygame.display.update()를 통해 파이게임을 동작시키고 프레임을 30으로 맞춰줍니다.
 
 ```buildoutcfg
 if __name__ == "__main__":
    main()
```
 
 <br>
 
  + Run시에 메인함수를 불러오면서 화면을 띄우고 시작하게 됩니다.
  
 ### 응용학습으로 벽밖으로 공이 나가지 않도록 해봅시다
 
[벽밖으로 못나가!](../GamePrac/Prac2.py)