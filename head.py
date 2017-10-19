import pygame, sys
from pygame import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Head Movement')


HEAD_WIDTH = 30
HEAD_HEIGHT = 30
headSpeedX = 1
p1head = pygame.Rect(320, 240, HEAD_WIDTH, HEAD_HEIGHT)
HEAD_COLOR = pygame.color.Color("red")
clock = pygame.time.Clock()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
textsurface = myfont.render('You lost', False, (0, 0, 0))

direction = (0,0) #right, down
running = True
while running:
    # clear screen with black color
    clock.tick(30)
    screen.fill( (0,0,0) )     #screen.fill(BLACK)
    p1head.left = p1head.left + headSpeedX*direction[0]
    p1head.top = p1head.top + headSpeedX*direction[1]
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                direction = (-1,0)
                #p1head.left = p1head.left - headSpeedX * 10
            if event.key == K_RIGHT:
                direction = (1,0)
                #p1head.left = p1head.left + headSpeedX * 10
            if event.key == K_UP:
                direction = (0,-1)
                #p1head.top = p1head.top - headSpeedX * 10
            if event.key == K_DOWN:
                direction = (0,1)
                #p1head.top = p1head.top + headSpeedX * 10
        if p1head.left <= 0 or p1head.left >= 640:
            screen.blit(textsurface,(0,0))
            running = False
        if p1head.top <= 0 or p1head.top >= 480:
            running = False
        if event.type == QUIT:                                         #write this one indent out to quit!
            pygame.quit()
            sys.exit()
            pygame.display.update()

    # draw the paddle
    screen.fill( HEAD_COLOR, p1head );

    pygame.display.update()
