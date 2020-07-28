import sys
from random import randint
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN,K_SPACE,K_F5,K_ESCAPE

pygame.init()
pygame.key.set_repeat(5,5) #키의 반복기능을 설정하는 pygame 의 메서드
SURFACE = pygame.display.set_mode((800,600))
FPSCLOCK = pygame.time.Clock()

def main():
    f= open("BestScore.txt", 'r') #Best 시간 불러오기 텍스트파일은 반드시 폴더에 같이 있어야 하므로 미리 만들기 바랍니다.
    BestScore = f.readline()#베스트 점수
    walls = 80 #동굴을 구성하는 직사각형의 수
    ship_y = 250 #내 캐릭터의 Y좌표
    velocity = 0 #내 캐릭터가 상하로 이동할 때의 속도
    score = 0 #점수
    slope = randint(1,6) #동굴의 기울기(옆의 직사각형과 Y축방향으로 얼마나 비켜잇는지)
    sysfont = pygame.font.SysFont(None,36)
    ship_image = pygame.image.load("./PyShooting/fighter1.png")
    bang_image = pygame.image.load("./PyShooting/explosion.png")
    holes = [] #동굴을 구성하는 직사각형을 저장하는 배열
    for xpos in range(walls): #동굴을 구성하는 직사각형 작성 코드
        holes.append(Rect(xpos*10, 100, 10, 400)) #Rect(X, Y, Width, Height)
    game_over = False #게임오버인지 아닌지 여부의 플래그

    while True:
        is_space_down =False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE: #Spacebar 누르면 캐릭이 위로올라감
                    is_space_down = True
                if event.key == K_F5: #F5키를 누르면 다시시작
                    game_over == False
                    main()
                if event.key == K_ESCAPE: #ESC키를 누르면 게임을 종료한다.
                    pygame.quit()
                    sys.exit()

        #내 캐릭터를 이동
        if not game_over:
            score+=10
            velocity += -3 if is_space_down else 3
            ship_y += velocity

            #동굴을 스크롤
            edge = holes[-1].copy()
            test =edge.move(0,slope) #rect를 움직이는 메서드
            if test.top <= 0 or test.bottom >=600: #천장에 닿았거나 혹은 바닥에 닿앗는지 검출
                slope = randint(1,6) * (-1 if slope >0 else 1)
                edge.inflate_ip(0,-20)

            edge.move_ip(10,slope)
            holes.append(edge) #맨끝 오른쪽에 직사각형 추가
            del holes[0] #맨앞 직사각형 삭제
            holes = [x.move(-10,0) for x in holes]

            #충돌?
            if holes[0].top > ship_y or holes[0].bottom <ship_y +50: #이값을 조절하여 충돌판정을 조정할 수 있다.
                game_over = True
        #그리기
        SURFACE.fill((0,255,0))
        for hole in holes:
            pygame.draw.rect(SURFACE,(0,0,0), hole)
        SURFACE.blit(ship_image,(0,ship_y))
        score_image = sysfont.render("score:{}".format(score),True,(0,0,225))
        BestScore_image = sysfont.render("BestScore:{}".format(BestScore), True, (0, 0, 225))
        SURFACE.blit(score_image, (600, 60)) #스코어를 표시한다
        SURFACE.blit(BestScore_image, (600, 20)) #현재 베스트 스코어를 표시한다.

        if game_over:
            SURFACE.blit(bang_image, (0,ship_y-40)) #비행기가 터지는 모습을 보여준다.
            if int(BestScore) <= score:#만약 score가 bestscore 보다 크다면 파일불러와서 Best 시간 기록
                BestScore = str(score)
                f = open("BestScore.txt", "w")#기존의 내용을 삭제하고 파일을 불러와서 내용기록
                f.write(str(BestScore))
                f.close

        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == "__main__":
    main()
