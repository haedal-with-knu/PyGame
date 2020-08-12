
import pygame
import sys
import random
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN


WIDTH = 600
HEIGHT = 600
pygame.init()
pygame.key.set_repeat(15, 15)
pygame.display.set_caption("Test")
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
FPSCLOCK = pygame.time.Clock()


def main():
    game_over = False
    pos_x = 300
    pos_y = 300
    rdx_posx = []
    rdx_posy = []
    rdy_posx = []
    rdy_posy = []
    velocity_y = []
    velocity_x = []
    for i in range(1,15):
        i *= 40
        rdx_posx.append(i)
        rdx_posy.append(0)
        velocity_y.append(random.randint(5, 12))
        rdy_posx.append(0)
        rdy_posy.append(i)
        velocity_x.append(random.randint(5, 12))

    while True:
        SURFACE.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    pos_x -= 10
                if event.key == K_RIGHT:
                    pos_x += 10
                if event.key == K_UP:
                    pos_y -= 10
                if event.key == K_DOWN:
                    pos_y += 10
        if game_over == True:
            pygame.quit()
            sys.exit()
        if pos_x > 580:
            pos_x = 580
        elif pos_x <20:
            pos_x =20
        if pos_y > 580:
            pos_y = 580
        elif pos_y <20:
            pos_y =20

        for i in range(len(rdx_posx)):
            pygame.draw.circle(SURFACE, (255, 255, 0), (rdx_posx[i], rdx_posy[i]), 2)
            pygame.draw.circle(SURFACE, (255, 255, 0), (rdy_posx[i], rdy_posy[i]), 2)
            if rdx_posy[i]<0 or rdx_posy[i] > 600 :
                velocity_y[i] *= -1
            if rdy_posx[i]<0 or rdy_posx[i] > 600 :
                velocity_x[i] *= -1
            rdx_posy[i] += velocity_y[i]
            rdy_posx[i] += velocity_x[i]

            #충돌 판정
            if (pos_x == rdx_posx[i] and pos_y == rdx_posy[i]) or (pos_x == rdy_posx[i] and pos_y == rdy_posy[i]):
                game_over = True
        pygame.draw.circle(SURFACE, (255, 255, 255), (pos_x, pos_y), 6)
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == "__main__":
    main()

