![지뢰찾기](../img/지뢰찾기.PNG)

우리가 어린시절에 하던 지뢰찾기원리와 같습니다. 단지 난이도가 많이 쉽습니다.

[지뢰찾기코드](../GamePrac/PyagameMine_sweeper.py)

### 코드알아보기

```buildoutcfg
while True:
    a = input("난이도를 몇으로 하시겠습니까? 1, 2, 3, 4:\n")
    if a == '1':
        WIDTH = 10
        HEIGHT = 10
        BOMBS = 10
        break
    elif a == '2':
        WIDTH = 15
        HEIGHT = 15
        BOMBS = 15
        break
    elif a == '3':
        WIDTH = 25
        HEIGHT = 20
        BOMBS = 22
        break
    elif a == '4':
        WIDTH = 30
        HEIGHT = 20
        BOMBS = 30
        break
    else:
        print("잘못입력하셨습니다, 1에서 4까지 다시 입력하세요\n")
        continue
```
<br>

게임실행전 난이도를 설정하기 위한 코드입니다. 
난이도를 조정해서 각자 맞는 실력에 게임을 실행할수있습니다.

<br>

```buildoutcfg
SIZE =30 #1칸의 가로세로 곱의 크기
EMPTY = 0 #맵상의 타일에 아무것도 없는 상태
BOMB = 1 #맵상의 타일에 폭탄이 있는 상태
OPENED =2 # 맵상의 타일이 이미 비어진 상태
OPEN_COUNT = 0 #열린 타일의 수

CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)] #타일의 상태를 이미 확인했는지 기록하는 배열
```

<br>

```buildoutcfg
def bomb(field, x_pos, y_pos):
    count = 0
    for yoffset in range(-1,2):
        for xoffset in range(-1,2):
            xpos, ypos = (x_pos + xoffset, y_pos+ yoffset)
            if 0 <=xpos <WIDTH and 0<=ypos <HEIGHT and field[ypos][xpos] == BOMB:
                count += 1
    return count
```

<br>
주변의 폭탄수를 세어나갑니다. 그리고 주위의 폭탄수를 반환하여 폭탄을 피할수있게 도와줍니다.
<br>

```buildoutcfg
def open_tile(field, x_pos, y_pos):
    global OPEN_COUNT
    if CHECKED[y_pos][x_pos]:
        return

    CHECKED[y_pos][x_pos] =True

    for yoffset in range(-1,2):
        for xoffset in range(-1,2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos] == EMPTY:
                field[ypos][xpos] = OPENED
                OPEN_COUNT += 1
                count = bomb(field,xpos,ypos)
                if count == 0 and not (xpos== x_pos and ypos == y_pos):
                    open_tile(field,xpos,ypos)
```

<br>
폭탄이 있는 칸 주위에 폭탄이 존재하지않는다면 주위의 칸을 열고 무한으로 같은 함수를
호출하지 않게 return값을 반환하여 탈출시킵니다. 그리고 빈타일이 클릭되면 인접하는 모든 빈타일이
일제히 open되게 해줍니다.
<br>

```buildoutcfg
field = [[EMPTY for xpos in range(WIDTH)] for ypos in range(HEIGHT)]
```

<br>

리스트내포 표기를 이중으로 해서 2차원 배열을 초기화합니다.

<br>


```buildoutcfg
    while True:
        for event in pygame.event.get():
            if event.type ==QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                xpos, ypos = floor(event.pos[0] / SIZE), floor(event.pos[1]/ SIZE)
                if field[ypos][xpos] == BOMB:
                    game_over = True
                else:
                    open_tile(field,xpos,ypos)
```

<br>

이벤트 타입이 quit이면 게임을 종료하고 마우스 왼쪽 버튼을 클릭하면 x 좌표와 y좌료를
size로 나누고 floor를 사용하여 정수로 표현합니다. 이렇게 구한 칸에 폭탄이있다면
게임오버를 알려주고 아니면 타일을 열어주고 있습니다.  

<br>

```buildoutcfg
#화면그리기
SURFACE.fill((0,0,0))
        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                tile = field[ypos][xpos]
                rect = (xpos*SIZE,ypos*SIZE,SIZE,SIZE)

                if tile == EMPTY or tile == BOMB:
                    pygame.draw.rect(SURFACE,(192,192,192),rect)
                    if game_over and tile == BOMB:
                        pygame.draw.ellipse(SURFACE,(225,225,0),rect)
                elif tile == OPENED:
                    count = bomb(field,xpos,ypos)
                    if count>0:
                        num_image = smallfont.render("{}".format(count),True,(255,255,0))
                        SURFACE.blit(num_image,(xpos*SIZE+10,ypos*SIZE+10))
```
<br>

```buildoutcfg
 # 선 그리기
        for index in range(0,WIDTH*SIZE, SIZE):
            pygame.draw.line(SURFACE, (96,96,96),(index,0),(index,HEIGHT*SIZE))

        for index in range(0, HEIGHT * SIZE, SIZE):
            pygame.draw.line(SURFACE,(96,96,96),(0,index),(WIDTH*SIZE,index))

        #메세지 나타내기
        if OPEN_COUNT == WIDTH *HEIGHT - BOMBS:
            SURFACE.blit(message_clear,message_rect.topleft)
        elif game_over:
            SURFACE.blit(message_over, message_rect.topleft)
            SURFACE.blit(message_F5, message_rect.bottomleft)
        pygame.display.update()
        FPSCLOCK.tick(15)
```

