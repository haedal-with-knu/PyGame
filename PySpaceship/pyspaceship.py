import gettext
import math
import random
import sys
from time import sleep

import pygame
from pygame.locals import *

WINDOW_WIDTH =800
WINDOW_HEIGHT = 600

BLACK =(0,0,0)
WHITE =(200,200,200)
YELLOW = (250,250,20)
BLUE =(20,20,250)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('PySpaceShip:우주 암석 피하기 게임')
pygame.display.set_icon(pygame.image.load('warp.png'))
fps_clock = pygame.time.Clock()
FPS = 60
score =0
default_font = pygame.font.Font('NanumGothic.ttf',28)
background_img = pygame.image.load('background.jpg')
explosion_sound = pygame.mixer.Sound('explosion.wav')
warp_sound = pygame.mixer.Sound('warp.wav')
pygame.mixer.music.load('Inner_Sanctum.mp3')

class SpaceShip(pygame.sprite.Sprite):
    def __init__(self):
        super(SpaceShip,self).__init__()
        self.image = pygame.image.load('spaceship.png')
        self.rect = self.image.get_rect()
        self.centerx = self.rect.centerx
        self.centery = self.rect.centery
    def set_pos(self,x,y):
        self.rect.x = x - self.centerx
        self.rect.y = y - self.centery
    def collide(self,sprites):
        for sprite in sprites:
            if pygame.sprite.collide_rect(self,sprite):
                return sprite

class Rock(pygame.sprite.Sprite):
    def __init__(self,xpos,ypos,hspeed,vspeed):
        super(Rock, self).__init__()
        rocks = ('rock01.png','rock02.png','rock03.png','rock04.png','rock05.png',\
                 'rock06.png','rock07.png','rock08.png','rock09.png','rock10.png',\
                 'rock11.png','rock12.png','rock13.png','rock14.png','rock15.png',\
                 'rock16.png','rock17.png','rock18.png','rock19.png','rock20.png',\
                 'rock21.png','rock22.png','rock23.png','rock24.png','rock25.png',\
                 'rock26.png','rock27.png','rock28.png','rock29.png','rock30.png')

        self.image = pygame.image.load(random.choice(rocks))
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.hspeed = hspeed
        self.vspeed = vspeed

        self.set_direction()

    def set_direction(self):
        if self.hspeed > 0:
            self.image = pygame.transform.rotate(self.image, 270)
        elif self.hspeed <0:
            self.image = pygame.transform.rotate(self.image, 90)
        elif self.vspeed >0:
            self.image = pygame.transform.rotate(self.image, 180)
    def update(self):
        self.rect.x += self.hspeed
        self.rect.y += self.vspeed
        if self.collide():
            self.kill()

    def collide(self):
        if self.rect.x <0 - self.rect.height or self.rect.x > WINDOW_WIDTH:
            return True
        elif self.rect.y<0 -self.rect.height or self.rect.y > WINDOW_HEIGHT:
            return True

def random_rock(speed):
    random_direction = random.randint(1,4)
    if random_direction ==1:
        return Rock(random.randint(0,WINDOW_WIDTH),0,0,speed)
    elif random_direction ==2:
        return Rock(WINDOW_WIDTH, random.randint(0,WINDOW_HEIGHT),-speed,0)
    elif random_direction ==3:
        return Rock(random.randint(0,WINDOW_WIDTH),WINDOW_HEIGHT,0,-speed)
    elif random_direction ==4:
        return Rock(0,random.randint(0,WINDOW_HEIGHT),speed,0)
class Warp(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Warp, self).__init__()
        self.image = pygame.image.load('warp.png')
        self.rect = self.image.get_rect()
        self.rectx = x-self.rect.centerx
        self.recty = y-self.rect.centery
def draw_repeating_background(background_img):
    background_rect = background_img.get_rect()
    for i in range(int(math.ceil(WINDOW_WIDTH/background_rect.width))):
        for j in range(int(math.ceil(WINDOW_HEIGHT/ background_rect.height))):
            screen.blit(background_img, Rect( i * background_rect.width,
                                              j * background_rect.height,
                                              background_rect.width,
                                              background_rect.height))
def draw_text(text, font, surface, x, y, main_color):
    text_obj = font.render(text, True,  main_color)
    text_rect = text_obj.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    surface.blit(text_obj, text_rect)

def game_loop():
    global score

    pygame.mixer.music.play(-1)#-1은 노래 무한반복
    pygame.mouse.set_visible(False)
    spaceship=SpaceShip()
    spaceship.set_pos(*pygame.mouse.get_pos())
    rocks = pygame.sprite.Group()
    warps = pygame.sprite.Group()
    min_rock_speed = 1
    max_rock_speed = 1
    occur_of_rocks = 1
    occur_prob = 15
    warp_count = 1
    paused =False

    while True:
        pygame.display.update()
        fps_clock.tick(FPS)
        if paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = not paused
                        pygame.mouse.set_visible(False)
                if event.type == QUIT:
                    return 'quit'
        else:
            draw_repeating_background(background_img)
            occur_of_rocks = 1 + int(score / 500)
            min_rock_speed = 1 + int(score / 400)
            max_rock_speed = 1 + int(score / 300)
            if random.randint(1, occur_prob) == 1:
                for i in range(occur_of_rocks):
                    rocks.add(random_rock(random.randint(min_rock_speed,max_rock_speed)))
                    score += 1
                if random.randint(1,occur_prob*10) == 1:
                    warp = Warp(random.randint(30,WINDOW_WIDTH-30),
                                random.randint(30,WINDOW_HEIGHT-30))
                    warps.add(warp)
            draw_text('점수 : {}'.format(score),default_font,screen,80,20,YELLOW)
            draw_text('워프 : {}'.format(warp_count), default_font, screen, 700, 20, BLUE)
            rocks.update()
            warps.update()
            rocks.draw(screen)
            warps.draw(screen)
            warp = spaceship.collide(warps)
            if spaceship.collide(rocks):
                explosion_sound.play()
                pygame.mixer.music.stop()
                rocks.empty()
                return 'game_screen'
            elif warp:
                warp_count +=1
                warp.kill()

            screen.blit(spaceship.image,spaceship.rect)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[0]<=10:
                        pygame.mouse.set_pos(WINDOW_WIDTH -10,mouse_pos[1])
                    elif mouse_pos[1]>=WINDOW_WIDTH -10:
                        pygame.mouse.set_pos(0+10,mouse_pos[1])
                    elif mouse_pos[1]<=10:
                        pygame.mouse.set_pos(mouse_pos[0],WINDOW_HEIGHT-10)
                    elif mouse_pos[1]>=WINDOW_HEIGHT-10:
                        pygame.mouse.set_pos(mouse_pos[0], 0+10)
                    spaceship.set_pos(*mouse_pos)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if warp_count >0:
                        warp_count -=1
                        warp_sound.play()
                        sleep(1)
                        rocks.empty()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = not paused
                        if paused:
                            transp_surf = pygame.Surface((WINDOW_WIDTH,WINDOW_HEIGHT))
                            transp_surf.set_alpha(150)
                            screen.blit(transp_surf,transp_surf.get_rect())
                            pygame.mouse.set.visible(True)
                            draw_text('일시정지',
                                      pygame.font.Font('NanumGothic.ttf',60),
                                      screen,WINDOW_WIDTH/2,WINDOW_HEIGHT/2,YELLOW)
                if event.type == QUIT:
                    return 'quit'

    return 'game_screen'
def game_screen():
    global score
    pygame.mouse.set_visible(True)

    start_image = pygame.image.load('game_screen.png')
    screen.blit(start_image,[0,0])

    draw_text('우주 암석 피하기',
              pygame.font.Font('NanumGothic.ttf',70),screen,
              WINDOW_WIDTH/2,WINDOW_HEIGHT/3.4,WHITE)
    draw_text('점수 : {}'.format(score),
              default_font, screen,
              WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2.4, YELLOW)
    draw_text('마우스 버튼이나 ''S''키를 누르면 게임이 시작됩니다.',
              default_font, screen,
              WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2.0, WHITE)
    draw_text('게임을 종료하시려면 ''Q''키를 누르세요.',
              default_font, screen,
              WINDOW_WIDTH / 2, WINDOW_HEIGHT / 1.8, WHITE)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_q:
                return 'quit'
            elif event.key== pygame.K_s:
                score =0
                return 'play'
        if event.type == pygame.MOUSEBUTTONDOWN:
            score =0
            return 'play'
        if event.type == QUIT:
            return 'quit'
    return 'game_screen'
def main_loop():
    action = 'game_screen'
    while action != 'quit':
        if action == 'game_screen':
            action = game_screen()
        elif action == 'play':
            action = game_loop()

    pygame.quit()

main_loop()
