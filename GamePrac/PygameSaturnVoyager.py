import sys
from random import randint
import pygame
from pygame.locals import QUIT, KEYDOWN,KEYUP, K_LEFT,K_RIGHT,K_UP,K_DOWN

pygame.init()
SURFACE = pygame.display.set_mode((800,800))
FPSCLOCK = pygame.time.Clock()

def main():
    game_over = False
    score = 0
    speed = 25
    stars =[] #운석을 저장하는 리스트
    keymap = [] #어느키가 입력돼 있는지를 나타내는 리스트
    ship = [0,0] #내 캐릭터의 좌표
    scope_image = pygame.image.load("img/scope.png")
    rock_image = pygame.image.load("img/rock.png")

    scorefont = pygame.font.SysFont(None, 36)
    sysfont =pygame.font.SysFont(None, 72)
    message_over = sysfont.render("Game Over!!",True,(0,255,255))
    message_rect = message_over.get_rect()
    message_rect.center = (400,400)

    while len(stars) < 200 :
        stars.append({"pos":[randint(-1600,1600),randint(-1600,1600),randint(0,4095)],
                      "theta":randint(0,360)})  #pos는 운석의좌표, theta는 회전각도

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN: #keymap이 없으면 keymap에 추가하는 코드
                if not event.key in keymap:
                    keymap.append(event.key)
            elif event.type == KEYUP: #keymap에 저장
                keymap.remove(event.key)

    #프레임별 처리
        if not game_over: # 프레임마다 score 를 1씩증가시키고 score가 십단위로 높아지면 스피드도 1씩올라감
            score += 1
            if score%10 == 0:
                speed +=1

            if K_LEFT in keymap:
                ship[0] -= 30

            elif K_RIGHT in keymap:
                ship[0] +=30

            elif K_UP in keymap:
                ship[1] -=30

            elif K_DOWN in keymap:
                ship[1] +=30

            ship[0] = max(-800,min(800,ship[0])) #좌표가 -800에서 800사이로 되도록 제한한다
            ship[1] = max(-800,min(800,ship[1]))

            for star in stars: #운석을 이동하는 코드
                star["pos"][2]-=speed
                if star["pos"][2] <64: #운석의 충돌을 알아보는 코드
                    if abs(star["pos"][0]- ship[0]) < 50 and abs(star["pos"][1]-ship[1]) < 50:
                        game_over = True
                    star["pos"] = [randint(-1600,1600),randint(-1600,1600),4095]

        #그리기
        SURFACE.fill((0,0,0))
        stars = sorted(stars, key = lambda x: x["pos"][2], reverse =True) #z좌표가 큰 순서대로 정렬하여 원근감을 표시
        for star in stars:
            zpos = star["pos"][2]
            xpos = ((star["pos"][0] - ship[0])<< 9 ) /zpos +400 #운석과 내캐릭터 간의 X축차이값을 구한다.
            ypos = ((star["pos"][1] - ship[1])<< 9 ) /zpos +400
            size = (50<<9) / zpos #shift연산자는 일반 곱보다 속도처리속도가 빨라서 shift연산 사용
            rotated = pygame.transform.rotozoom(rock_image, star["theta"], size/145)
            SURFACE.blit(rotated, (xpos,ypos))

        SURFACE.blit(scope_image,(0,0))

        if game_over:
            SURFACE.blit(message_over, message_rect)
            pygame.mixer.music.stop()

        #점수 나타내기
        score_str = str(score).zfill(6) #대상이 되는 문자열의 왼쪽을 0으로 채워주는 메소드 (자릿수정렬)
        score_image = scorefont.render(score_str,True,(0,255,0))
        SURFACE.blit(score_image,(700,50))
        pygame.display.update()
        FPSCLOCK.tick(20)

if __name__ == "__main__":
    main()