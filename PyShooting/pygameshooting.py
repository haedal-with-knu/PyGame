import pygame
import sys
import random
from time import sleep



padWidth =480 #게임가로화면
padHeight = 640 #게임세로화면
rockImage = ['rock01.png','rock02.png','rock03.png','rock04.png','rock05.png',\
             'rock06.png','rock07.png','rock08.png','rock09.png','rock10.png',\
             'rock11.png','rock12.png','rock13.png','rock14.png','rock15.png',\
             'rock16.png','rock17.png','rock18.png','rock19.png','rock20.png',\
             'rock21.png','rock22.png','rock23.png','rock24.png','rock25.png',\
             'rock26.png','rock27.png','rock28.png','rock29.png','rock30.png']
explosionSound = ['explosion01.wav','explosion02.wav','explosion03.wav','explosion04.wav']
pygame.font.init()
#맞춘운석수 갯수
def writeScore(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf',20)
    text = font.render('파괴한운석수:' +str(count),True,(255,255,255))
    gamePad.blit(text,(10,0))
#운석이 화면아래로 통과한 갯수
def writePassed(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf',20)
    text = font.render('놓친운석수:' +str(count),True,(255,0,0))
    gamePad.blit(text,(360,0))

def writeMessage(text):
    global gamePad, gameOverSound
    textfont = pygame.font.Font('NanumGothic.ttf',80)
    text =textfont.render(text,True,(255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text,textpos)
    pygame.display.update()
    pygame.mixer.music.stop()
    gameOverSound.play()
    sleep(2)
    pygame.mixer.music.play(-1)
    runGame()

def crash():
    global gamePad
    writeMessage('전투기파괴!')
def gameOver():
    global gamePad
    writeMessage('게임오버!')


#게임에 등장하는 객체를 드로잉
def drawObject(obj,x,y):
    global gamePad
    gamePad.blit(obj,(x,y))

#In game 게임화면 구성
def iniGame():
    global gamePad, clock, background, fighter,missile, explosion,missileSound,gameOverSound
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth,padHeight))
    pygame.display.set_caption('pygameshooting')
    background =pygame.image.load('background.png')#배경그림
    fighter = pygame.image.load('fighter.png')#전투기 그림
    missile = pygame.image.load('missile.png')#미사일 그림
    explosion = pygame.image.load('explosion.png')#폭발그림
    pygame.mixer.music.load('music.wav')
    pygame.mixer.music.play(-1)
    missileSound = pygame.mixer.Sound('missile.wav')
    gameOverSound = pygame.mixer.Sound('gameOver.wav')
    clock = pygame.time.Clock()


def runGame():
    global gamePad, clock, background, fighter , missile, explosion, missileSound

    #전투기크기 및 초기위치(x,y)
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    x = padWidth * 0.45
    y = padHeight * 0.9
    fighterX = 0
    #무기 좌표 리스트
    missileXY = []
    #운석 랜덤생성
    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size #운석크기
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    destroySound = pygame.mixer.Sound(random.choice(explosionSound))

    #운석초기 위치 설정
    if padWidth - rockWidth>0:
        rockX = random.randrange(0, padWidth - rockWidth)
        rockY = 0
        rockSpeed =2
        #전투기 미사일에 운석이 맞앗을 경우True
        isShot = False
        shotCount = 0
        rockPassed = 0

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:#게임프로그램종료 창을닫으면 시스템자체종료 코드
                pygame.quit()
                sys.exit()
            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT: #전투기왼쪽으로 이동
                    fighterX -=5

                elif event.key == pygame.K_RIGHT: #전투기를 오른쪽으로 이동
                    fighterX +=5

                elif event.key == pygame.K_SPACE:#미사일발사
                    missileSound.play()
                    missileX = x + fighterWidth/2 #미사일이 전투기의 중간에서 발사됨 
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])

            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #키를 떄면 전투기가 멈
                    fighterX = 0

        drawObject(background, 0, 0) #배경화면 그리기

        x += fighterX # 전투기위치를 재조정하기
        if x<0:#게임화면 왼쪽끝
            x=0
        elif x> padWidth - fighterWidth: #게임화면 오른쪽끝
            x = padWidth - fighterWidth

        #전투기가 운석과 충돌했는지 체크
        if y <rockY + rockHeight:
            if(rockX>x and rockX< x+ fighterWidth) or (rockX +rockWidth >x and rockX + rockWidth < x+ fighterWidth):
                crash()

        drawObject(fighter, x, y) #비행기를 게임화면의(x,y)좌표에 그리기

        if len(missileXY) != 0:
            for i , bxy in enumerate(missileXY): #미사일요소에 대해서 반복함
                bxy[1] -=10 #총알의 y좌표 -10(위로이동)
                missileXY[i][1] = bxy[1]

                #미사일이 운석을 맞췄을때
                if bxy[1]<rockY:
                    if bxy[0] > rockX and bxy[0]<rockX+rockWidth:
                        missileXY.remove(bxy)
                        isShot =True
                        shotCount +=1
                
                if bxy[1]<=0:#미사일이 화면밖으로 벗어나면
                    try:
                        missileXY.remove(bxy)#미사일제거
                    except:
                        pass

        if len(missileXY) !=0:
            for bx,by in missileXY:
                drawObject(missile, bx,by)
        writeScore(shotCount)
        rockY +=rockSpeed

        if rockY>padHeight:
            if padWidth - rockWidth>0:
                #새로운 운석(랜덤)
                rock = pygame.image.load(random.choice(rockImage))
                rockSize = rock.get_rect().size #운석크기
                rockWidth = rockSize[0]
                rockHeight = rockSize[1]
                

                #운석초기 위치 설정
                rockX = random.randrange(0, padWidth - rockWidth)
                #rockX = 1
                rockY = 0
                rockPassed += 1
        if rockPassed ==4:
            gameOver()
        #놓친운석의 수 표시
                
        writePassed(rockPassed)
            #운석을 맞춘경우
        if isShot:
            drawObject(explosion, rockX,rockY)
            destroySound.play()
            if padWidth - rockWidth>0:
                #새로운 운석(랜덤)
                rock = pygame.image.load(random.choice(rockImage))
                rockSize = rock.get_rect().size #운석크기
                rockWidth = rockSize[0]
                rockHeight = rockSize[1]

                #운석초기 위치 설정

                rockX = random.randrange(0, padWidth - rockWidth)
                rockY = 0
                destroySound = pygame.mixer.Sound(random.choice(explosionSound))
                isShot = False

            #운석을 맞추면 속도증가
            rockSpeed +=0.2
            if rockSpeed>=10:
                rockSpeed=10
        
        drawObject(rock,rockX,rockY)

        
        pygame.display.update() #게임화면을 다시그림

        clock.tick(60) #게임화면의 초당 프레임수를 60으로 설정
    pygame.quit() #pygame 종료

iniGame()
runGame()


